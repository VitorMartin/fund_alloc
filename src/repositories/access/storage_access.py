import os
import shutil
from typing import Any, List

import pyodbc

from src.interfaces.i_storage import IStorage
from src.models.amort_desemb import AmortDesemb
from src.models.amort_fund import AmortFund
from src.models.desemb import Desemb
from src.models.enums.dict_keys import *
from src.models.fund import Fund
from src.repositories.access.en_tables import TABLE
from src.repositories.errors.repository_error import NotFoundError, RepositoryError


class StorageAccess(IStorage):
    __connectionStr: str
    __dbFilename: str
    __dbPath: str
    __connection: pyodbc.Connection
    __cursor: pyodbc.Cursor

    def __init__(self):
        self.__dbPath = os.path.dirname(__file__)
        self.__dbFilename = 'db.accdb'
        self.__dbBkpFilename = 'db_bkp.accdb'
        self.__connectionStr = (
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                r'DBQ=' + os.path.join(self.__dbPath, self.__dbFilename)
        )
        try:
            self.__connection = pyodbc.connect(self.__connectionStr)
        except pyodbc.Error:
            shutil.copy(
                os.path.join(self.__dbPath, self.__dbBkpFilename),
                os.path.join(self.__dbPath, self.__dbFilename)
            )
            self.__connection = pyodbc.connect(self.__connectionStr)

        self.__cursor = self.__connection.cursor()

    def customQuery(self, sql: str, params: Any = None) -> List[Any]:
        if params:
            self.__cursor.execute(sql, params)
        else:
            self.__cursor.execute(sql)
        return self.__cursor.fetchall()

    def parseRow(self, model: MODEL, row) -> Any:
        obj = {}

        if model == MODEL.FUND:
            self.__cursor.execute(f'SELECT * FROM {TABLE.FUNDS}')
            fundColumns = [column[0] for column in self.__cursor.description]
            dFund = dict(zip(fundColumns, row))

            dFund[FUND.INI.value] = dFund[FUND.INI.value].date()
            dFund[FUND.VENC.value] = dFund[FUND.VENC.value].date()

            obj = Fund.fromDict(dFund)

        elif model == MODEL.DESEMB:
            self.__cursor.execute(f'SELECT * FROM {TABLE.DESEMBS}')
            desembColumns = [column[0] for column in self.__cursor.description]
            dDesemb = dict(zip(desembColumns, row))

            sql = f'SELECT * FROM {TABLE.FUNDS} WHERE {FUND.ID} = ?fund_deal_id?'
            if dDesemb[DESEMB.FUND_ID.value] is None:
                sql = sql.replace('?fund_deal_id?', 'null')

            else:
                sql = sql.replace('?fund_deal_id?', str(dDesemb[DESEMB.FUND_ID.value]))

            self.__cursor.execute(sql)
            fundColumns = [column[0] for column in self.__cursor.description]

            result = self.__cursor.fetchone()
            if result is None:
                dFund = {}
            else:
                dFund = dict(zip(fundColumns, result))
                dFund[FUND.INI.value] = dFund[FUND.INI.value].date()
                dFund[FUND.VENC.value] = dFund[FUND.VENC.value].date()

            dJoin = dFund | dDesemb

            dJoin[DESEMB.INI.value] = dJoin[DESEMB.INI.value].date()
            dJoin[DESEMB.VENC.value] = dJoin[DESEMB.VENC.value].date()

            obj = Desemb.fromDict(dJoin)

        elif model == MODEL.AMORT_FUND:
            self.__cursor.execute(f'SELECT * FROM {TABLE.AMORT_FUNDS}')
            amortFundColumns = [column[0] for column in self.__cursor.description]
            dAmortFund = dict(zip(amortFundColumns, row))
            self.__cursor.execute(
                f'SELECT * FROM {TABLE.FUNDS} WHERE {AMORT_FUND.FUND_ID} = {dAmortFund[AMORT_FUND.FUND_ID.value]}'
            )
            fundColumns = [column[0] for column in self.__cursor.description]
            dFund = dict(zip(fundColumns, self.__cursor.fetchone()))
            dJoin = dFund | dAmortFund

            dJoin[FUND.INI.value] = dJoin[FUND.INI.value].date()
            dJoin[FUND.VENC.value] = dJoin[FUND.VENC.value].date()
            dJoin[AMORT_FUND.DATA.value] = dJoin[AMORT_FUND.DATA.value].date()

            obj = AmortFund.fromDict(dJoin)

        elif model == MODEL.AMORT_DESEMB:
            self.__cursor.execute(f'SELECT * FROM {TABLE.AMORT_DESEMBS}')
            amortDesembColumns = [column[0] for column in self.__cursor.description]
            dAmortDesemb = dict(zip(amortDesembColumns, row))
            self.__cursor.execute(
                f'SELECT * FROM {TABLE.DESEMBS} '
                f'WHERE {AMORT_DESEMB.DESEMB_ID} = {dAmortDesemb[AMORT_DESEMB.DESEMB_ID.value]}'
            )
            desembColumns = [column[0] for column in self.__cursor.description]
            dDesemb = dict(zip(desembColumns, self.__cursor.fetchone()))

            if dDesemb[DESEMB.FUND_ID.value] is None:
                dFund = {}
            else:
                self.__cursor.execute(
                    f'SELECT * FROM {TABLE.FUNDS} '
                    f'WHERE {DESEMB.FUND_ID} = {dDesemb[DESEMB.FUND_ID.value]}'
                )
                fundColumns = [column[0] for column in self.__cursor.description]
                dFund = dict(zip(fundColumns, self.__cursor.fetchone()))
                dFund[FUND.INI.value] = dFund[FUND.INI.value].date()
                dFund[FUND.VENC.value] = dFund[FUND.VENC.value].date()

            dJoin = dFund | dDesemb | dAmortDesemb

            dJoin[DESEMB.INI.value] = dJoin[DESEMB.INI.value].date()
            dJoin[DESEMB.VENC.value] = dJoin[DESEMB.VENC.value].date()
            dJoin[AMORT_DESEMB.DATA.value] = dJoin[AMORT_DESEMB.DATA.value].date()

            obj = AmortDesemb.fromDict(dJoin)

        return obj

    def getAllFunds(self) -> List[Fund]:
        self.__cursor.execute(f'SELECT * FROM {TABLE.FUNDS.value}')

        funds = []
        for row in self.__cursor.fetchall():
            funds.append(self.parseRow(MODEL.FUND, row))

        return funds

    def getAllDesembs(self) -> List[Desemb]:
        self.__cursor.execute(f'SELECT * FROM {TABLE.DESEMBS.value}')

        desembs = []
        for row in self.__cursor.fetchall():
            desembs.append(self.parseRow(MODEL.DESEMB, row))

        return desembs

    def getAllAmortFunds(self) -> List[AmortFund]:
        self.__cursor.execute(f'SELECT * FROM {TABLE.AMORT_FUNDS.value}')

        amortFunds = []
        for row in self.__cursor.fetchall():
            amortFunds.append(self.parseRow(MODEL.AMORT_FUND, row))

        return amortFunds

    def getAllAmortDesembs(self) -> List[AmortDesemb]:
        self.__cursor.execute(f'SELECT * FROM {TABLE.AMORT_DESEMBS.value}')

        amortDesembs = []
        for row in self.__cursor.fetchall():
            amortDesembs.append(self.parseRow(MODEL.AMORT_DESEMB, row))

        return amortDesembs

    def getDesembsInFundByKold(self, kold: str) -> List[Desemb]:
        self.__cursor.execute(
            f'SELECT * '
            f'FROM {TABLE.DESEMBS} INNER JOIN {TABLE.FUNDS} '
            f'ON {TABLE.FUNDS}.{FUND.ID} = {TABLE.DESEMBS}.{DESEMB.FUND_ID} '
            f'WHERE {TABLE.FUNDS}.{FUND.KOLD} = \'{kold}\' '
            f'ORDER BY {TABLE.DESEMBS}.{DESEMB.VENC}'
        )

        columns = [column[0] for column in self.__cursor.description]
        desembs = []
        for desemb in self.__cursor.fetchall():
            d = dict(zip(columns, desemb))
            d[FUND.INI.value] = d[FUND.INI.value].date()
            d[FUND.VENC.value] = d[FUND.VENC.value].date()
            d[DESEMB.INI.value] = d[DESEMB.INI.value].date()
            d[DESEMB.VENC.value] = d[DESEMB.VENC.value].date()
            desembs.append(Desemb.fromDict(d))

        return desembs

    def getFundById(self, dealId: int) -> Fund:
        self.__cursor.execute(f'SELECT * FROM {TABLE.FUNDS} WHERE {FUND.ID} = {dealId}')
        columns = [column[0] for column in self.__cursor.description]
        d = dict(zip(columns, self.__cursor.fetchone()))
        d[FUND.INI.value] = d[FUND.INI.value].date()
        d[FUND.VENC.value] = d[FUND.VENC.value].date()

        if bool(d):
            return Fund.fromDict(d)
        else:
            raise NotFoundError

    def getFundByKold(self, kold: str) -> Fund:
        self.__cursor.execute(f'SELECT * FROM {TABLE.FUNDS} WHERE {FUND.KOLD} = \'{kold}\'')
        columns = [column[0] for column in self.__cursor.description]
        result = self.__cursor.fetchone()
        if bool(result):
            d = dict(zip(columns, result))
            d[FUND.INI.value] = d[FUND.INI.value].date()
            d[FUND.VENC.value] = d[FUND.VENC.value].date()

            return Fund.fromDict(d)
        else:
            raise NotFoundError

    def getDesembById(self, dealId: int) -> Desemb:
        # Fetching desemb
        self.__cursor.execute(f'SELECT * FROM {TABLE.DESEMBS} WHERE {DESEMB.ID} = {dealId}')
        colsDesemb = [column[0] for column in self.__cursor.description]
        dDesemb = dict(zip(colsDesemb, self.__cursor.fetchone()))

        # Fetching Fund by fund_id
        self.__cursor.execute(f'SELECT * FROM {TABLE.FUNDS} WHERE {FUND.ID} = {dDesemb[DESEMB.FUND_ID.value]}')
        colsFund = [column[0] for column in self.__cursor.description]
        dFund = dict(zip(colsFund, self.__cursor.fetchone()))

        dJoin = dFund | dDesemb

        dJoin[FUND.INI.value] = dJoin[FUND.INI.value].date()
        dJoin[FUND.VENC.value] = dJoin[FUND.VENC.value].date()
        dJoin[DESEMB.INI.value] = dJoin[DESEMB.INI.value].date()
        dJoin[DESEMB.VENC.value] = dJoin[DESEMB.VENC.value].date()

        if bool(dJoin):
            return Desemb.fromDict(dJoin)
        else:
            raise NotFoundError

    def getDesembByCcb(self, ccb: str) -> Desemb:
        # Fetching desemb
        self.__cursor.execute(f'SELECT * FROM {TABLE.DESEMBS} WHERE {DESEMB.CCB} = \'{ccb}\'')
        colsDesemb = [column[0] for column in self.__cursor.description]
        result = self.__cursor.fetchone()
        if not result:
            raise NotFoundError
        dDesemb = dict(zip(colsDesemb, result))

        # Fetching Fund by fund_id
        if not dDesemb[DESEMB.FUND_ID.value]:
            dDesemb[DESEMB.INI.value] = dDesemb[DESEMB.INI.value].date()
            dDesemb[DESEMB.VENC.value] = dDesemb[DESEMB.VENC.value].date()
            return Desemb.fromDict(dDesemb)

        self.__cursor.execute(f'SELECT * FROM {TABLE.FUNDS} WHERE {FUND.ID} = {dDesemb[DESEMB.FUND_ID.value]}')
        colsFund = [column[0] for column in self.__cursor.description]
        dFund = dict(zip(colsFund, self.__cursor.fetchone()))

        dJoin = dFund | dDesemb

        dJoin[FUND.INI.value] = dJoin[FUND.INI.value].date()
        dJoin[FUND.VENC.value] = dJoin[FUND.VENC.value].date()
        dJoin[DESEMB.INI.value] = dJoin[DESEMB.INI.value].date()
        dJoin[DESEMB.VENC.value] = dJoin[DESEMB.VENC.value].date()

        if bool(dJoin):
            return Desemb.fromDict(dJoin)
        else:
            raise NotFoundError

    def getAmortFundById(self, amortId: int) -> AmortFund:
        # Fetching amort fund
        self.__cursor.execute(f'SELECT * FROM {TABLE.AMORT_FUNDS} WHERE {AMORT_FUND.ID} = {amortId}')
        colsAmortFund = [column[0] for column in self.__cursor.description]
        dAmortFund = dict(zip(colsAmortFund, self.__cursor.fetchone()))

        # Fetching Fund by fund_id
        self.__cursor.execute(f'SELECT * FROM {TABLE.FUNDS} WHERE {FUND.ID} = {dAmortFund[AMORT_FUND.FUND_ID.value]}')
        colsFund = [column[0] for column in self.__cursor.description]
        dFund = dict(zip(colsFund, self.__cursor.fetchone()))

        dJoin = dFund | dAmortFund

        dJoin[FUND.INI.value] = dJoin[FUND.INI.value].date()
        dJoin[FUND.VENC.value] = dJoin[FUND.VENC.value].date()
        dJoin[AMORT_FUND.DATA.value] = dJoin[AMORT_FUND.DATA.value].date()

        if bool(dJoin):
            return AmortFund.fromDict(dJoin)
        else:
            raise NotFoundError

    def getAmortFundsByFundId(self, dealId: int) -> List[AmortFund]:
        # Fetching amort funds
        self.__cursor.execute(f'SELECT * FROM {TABLE.AMORT_FUNDS} WHERE {AMORT_FUND.FUND_ID} = {dealId}')
        colsAmortFund = [column[0] for column in self.__cursor.description]
        rows = self.__cursor.fetchall()
        lAmortFunds = []
        for row in rows:
            dAmortFund = dict(zip(colsAmortFund, row))

            # Fetching Fund by fund_id
            self.__cursor.execute(
                f'SELECT * FROM {TABLE.FUNDS} WHERE {FUND.ID} = {dAmortFund[AMORT_FUND.FUND_ID.value]}'
            )
            colsFund = [column[0] for column in self.__cursor.description]
            dFund = dict(zip(colsFund, self.__cursor.fetchone()))

            dJoin = dFund | dAmortFund

            dJoin[FUND.INI.value] = dJoin[FUND.INI.value].date()
            dJoin[FUND.VENC.value] = dJoin[FUND.VENC.value].date()
            dJoin[AMORT_FUND.DATA.value] = dJoin[AMORT_FUND.DATA.value].date()

            lAmortFunds.append(dJoin)

        retAmortFunds = []
        for amort in lAmortFunds:
            retAmortFunds.append(AmortFund.fromDict(amort))

        if bool(retAmortFunds):
            return retAmortFunds
        else:
            raise NotFoundError

    def getAmortDesembById(self, amortId: int) -> AmortDesemb:
        # Fetching amort desemb
        self.__cursor.execute(f'SELECT * FROM {TABLE.AMORT_DESEMBS} WHERE {AMORT_DESEMB.ID} = {amortId}')
        colsAmortDesemb = [column[0] for column in self.__cursor.description]
        dAmortDesemb = dict(zip(colsAmortDesemb, self.__cursor.fetchone()))

        # Fetching Desemb
        self.__cursor.execute(
            f'SELECT * FROM {TABLE.DESEMBS} WHERE {DESEMB.ID} = {dAmortDesemb[AMORT_DESEMB.DESEMB_ID.value]}'
        )
        colsDesemb = [column[0] for column in self.__cursor.description]
        dDesemb = dict(zip(colsDesemb, self.__cursor.fetchone()))

        # Fetching Fund
        self.__cursor.execute(
            f'SELECT * FROM {TABLE.FUNDS} WHERE {FUND.ID} = {dDesemb[DESEMB.FUND_ID.value]}'
        )
        colsFund = [column[0] for column in self.__cursor.description]
        dFund = dict(zip(colsFund, self.__cursor.fetchone()))

        dJoin = dFund | dDesemb | dAmortDesemb

        dJoin[FUND.INI.value] = dJoin[FUND.INI.value].date()
        dJoin[FUND.VENC.value] = dJoin[FUND.VENC.value].date()
        dJoin[DESEMB.INI.value] = dJoin[DESEMB.INI.value].date()
        dJoin[DESEMB.VENC.value] = dJoin[DESEMB.VENC.value].date()
        dJoin[AMORT_DESEMB.DATA.value] = dJoin[AMORT_DESEMB.DATA.value].date()

        if bool(dJoin):
            return AmortDesemb.fromDict(dJoin)
        else:
            raise NotFoundError

    def getAmortDesembsByDesembId(self, dealId: int) -> List[AmortDesemb]:
        # Fetching amort desemb
        self.__cursor.execute(f'SELECT * FROM {TABLE.AMORT_DESEMBS} WHERE {AMORT_DESEMB.DESEMB_ID} = {dealId}')
        colsAmortDesemb = [column[0] for column in self.__cursor.description]
        rows = self.__cursor.fetchall()
        lAmortDesembs = []
        for row in rows:
            dAmortDesemb = dict(zip(colsAmortDesemb, row))

            # Fetching Desemb
            self.__cursor.execute(
                f'SELECT * FROM {TABLE.DESEMBS} WHERE {DESEMB.ID} = {dAmortDesemb[AMORT_DESEMB.DESEMB_ID.value]}'
            )
            colsDesemb = [column[0] for column in self.__cursor.description]
            dDesemb = dict(zip(colsDesemb, self.__cursor.fetchone()))

            # Fetching Fund
            if dDesemb[DESEMB.FUND_ID.value] is None:
                dFund = {}
            else:
                self.__cursor.execute(
                    f'SELECT * FROM {TABLE.FUNDS} WHERE {FUND.ID} = {dDesemb[DESEMB.FUND_ID.value]}'
                )
                colsFund = [column[0] for column in self.__cursor.description]
                dFund = dict(zip(colsFund, self.__cursor.fetchone()))
                dFund[FUND.INI.value] = dFund[FUND.INI.value].date()
                dFund[FUND.VENC.value] = dFund[FUND.VENC.value].date()

            dJoin = dFund | dDesemb | dAmortDesemb

            dJoin[DESEMB.INI.value] = dJoin[DESEMB.INI.value].date()
            dJoin[DESEMB.VENC.value] = dJoin[DESEMB.VENC.value].date()
            dJoin[AMORT_DESEMB.DATA.value] = dJoin[AMORT_DESEMB.DATA.value].date()

            lAmortDesembs.append(dJoin)

        retAmortDesembs = []
        for amort in lAmortDesembs:
            retAmortDesembs.append(AmortDesemb.fromDict(amort))

        if bool(retAmortDesembs):
            return retAmortDesembs
        else:
            raise NotFoundError

    # def getFundPrincAfterAmortById(self, dealId: int, basedate: date = date.today()) -> float:
    #     pass

    # def getDesembPrincAfterAmortById(self, dealId: int, basedate: date = date.today()) -> float:
    #     pass

    # def getAvailableFundsForDesembByCcb(self, ccb: str, basedate: date = date.today()) -> List[Fund]:
    #     pass

    # def getAmortsInFundByKold(self, kold: str) -> List[Amort]:
    #     pass

    # def generateFundFlowByKold(self, kold: str) \
    #         -> List[dict[Any, str, date, float, float, float, float, float]]:
    #     pass

    def changeFund(self, desemb, newFund):
        fundId = newFund.dealId if newFund is not None else 'null'
        try:
            self.__cursor.execute(
                f'UPDATE {TABLE.DESEMBS} SET {DESEMB.FUND_ID} = {fundId} WHERE {DESEMB.ID} = {desemb.dealId}'
            )
            self.__cursor.commit()
        except pyodbc.Error as e:
            raise RepositoryError(e)
        else:
            return self.getDesembByCcb(desemb.ccb)

    def createFund(self, fund: Fund, amorts: List[AmortFund]):
        # Insert Fund
        try:
            self.__cursor.execute(
                f'INSERT INTO {TABLE.FUNDS} ('
                f'  {FUND.KOLD}, {FUND.CCY}, {FUND.PRINC}, {FUND.INI}, {FUND.VENC}'
                f') '
                f'VALUES ('
                f'  \'{fund.kold}\', \'{fund.ccy}\', {fund.princ}, \'{fund.ini}\', \'{fund.venc}\''
                f')'
            )
            self.__cursor.commit()
            fund = self.getFundByKold(fund.kold)
        except pyodbc.Error as e:
            raise RepositoryError(e)

        # Insert Amort Funds
        for amort_fund in amorts:
            amort_fund.fund = fund
            try:
                self.__cursor.execute(
                    f'INSERT INTO {TABLE.AMORT_FUNDS} ('
                    f'  {AMORT_FUND.FUND_ID}, {AMORT_FUND.DATA}, {AMORT_FUND.CCY}, {AMORT_FUND.VAL}'
                    f') '
                    f'VALUES ('
                    f'  {amort_fund.fund.dealId}, \'{amort_fund.data.isoformat()}\', \'{amort_fund.ccy}\', {amort_fund.val}'
                    f')'
                )
                self.__cursor.commit()
            except pyodbc.Error as e:
                raise RepositoryError(e)

        return self.getFundByKold(fund.kold)

    def createDesemb(self, desemb: Desemb, amorts: List[AmortDesemb]):
        sql = (
            f'INSERT INTO {TABLE.DESEMBS} ('
            f'  {DESEMB.FUND_ID}, {DESEMB.CCB}, {DESEMB.CCY},'
            f'  {DESEMB.PRINC}, {DESEMB.INI}, {DESEMB.VENC}'
            f') '
            f'VALUES ('
            f'  ?fund_deal_id?, \'{desemb.ccb}\', \'{desemb.ccy}\','
            f'  {desemb.princ}, \'{desemb.ini}\', \'{desemb.venc}\''
            f')'
        )
        if desemb.fund:
            desemb.fund = self.getFundByKold(desemb.fund.kold)
            sql = sql.replace('?fund_deal_id?', str(desemb.fund.dealId))
        else:
            sql = sql.replace('?fund_deal_id?', 'null')

        # Insert Desemb
        try:
            self.__cursor.execute(sql)
            self.__cursor.commit()
            desemb = self.getDesembByCcb(desemb.ccb)
        except pyodbc.Error as e:
            raise RepositoryError(e)

        # Insert Amort Funds
        for amort_desemb in amorts:
            amort_desemb.desemb = desemb
            try:
                self.__cursor.execute(
                    f'INSERT INTO {TABLE.AMORT_DESEMBS} ('
                    f'  {AMORT_DESEMB.DESEMB_ID}, {AMORT_DESEMB.DATA}, {AMORT_DESEMB.CCY}, {AMORT_DESEMB.VAL}'
                    f') '
                    f'VALUES ('
                    f'  {amort_desemb.desemb.dealId}, \'{amort_desemb.data}\', \'{amort_desemb.ccy}\', {amort_desemb.val}'
                    f')'
                )
                self.__cursor.commit()
            except pyodbc.Error as e:
                raise RepositoryError(e)

        return self.getDesembByCcb(desemb.ccb)
