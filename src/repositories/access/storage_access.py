import os
from typing import Any, List
from datetime import date

import pyodbc

from src.interfaces.i_storage import IStorage
from src.models.amort_desemb import AmortDesemb
from src.models.amort_fund import AmortFund
from src.models.desemb import Desemb
from src.models.enums.dict_keys import *
from src.models.fund import Fund
from src.repositories.access.en_tables import TABLE


class StorageAccess(IStorage):
    __connectionStr: str
    __dbFilename: str
    __dbPath: str
    __connection: pyodbc.Connection
    __cursor: pyodbc.Cursor

    def __init__(self):
        self.__dbFilename = 'db.accdb'
        self.__dbPath = os.path.join(os.path.dirname(__file__), self.__dbFilename)
        self.__connectionStr = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=' + self.__dbPath
        )
        self.__connection = pyodbc.connect(self.__connectionStr)
        self.__cursor = self.__connection.cursor()

    def customQuery(self, sql: str, params: Any = None) -> List[Any]:
        if params:
            self.__cursor.execute(sql, params)
        else:
            self.__cursor.execute(sql)
        return self.__cursor.fetchall()

    def getAllFunds(self) -> List[Fund]:
        self.__cursor.execute(f'SELECT * FROM {TABLE.FUNDS.value}')

        columns = [column[0] for column in self.__cursor.description]
        funds = []
        for row in self.__cursor.fetchall():
            d = dict(zip(columns, row))
            d[FUND.INI.value] = d[FUND.INI.value].date()
            d[FUND.VENC.value] = d[FUND.VENC.value].date()
            funds.append(Fund.fromDict(d))

        return funds

    def getAllDesembs(self) -> List[Desemb]:
        self.__cursor.execute(f'SELECT * FROM {TABLE.DESEMBS.value}')

        desembs = []
        rows = self.__cursor.fetchall()
        colsDesemb = [column[0] for column in self.__cursor.description]
        for desemb in rows:
            dDesemb = dict(zip(colsDesemb, desemb))

            # Fetching Fund from fund_id
            self.__cursor.execute(f'SELECT * FROM {TABLE.FUNDS} WHERE {FUND.ID} = {dDesemb[FUND.ID.value]}')
            row = self.__cursor.fetchone()
            colsFund = [column[0] for column in self.__cursor.description]
            dFund = dict(zip(colsFund, row))

            dJoin = dFund | dDesemb

            dJoin[FUND.INI.value] = dJoin[FUND.INI.value].date()
            dJoin[FUND.VENC.value] = dJoin[FUND.VENC.value].date()
            dJoin[DESEMB.INI.value] = dJoin[DESEMB.INI.value].date()
            dJoin[DESEMB.VENC.value] = dJoin[DESEMB.VENC.value].date()
            desembs.append(Desemb.fromDict(dJoin))

        return desembs

    def getAllAmortFunds(self) -> List[AmortFund]:
        self.__cursor.execute(f'SELECT * FROM {TABLE.AMORT_FUNDS.value}')

        amortFunds = []
        rows = self.__cursor.fetchall()
        colsAmortFund = [column[0] for column in self.__cursor.description]
        for amortFund in rows:
            dAmortFund = dict(zip(colsAmortFund, amortFund))

            # Fetching Fund from fund_id
            self.__cursor.execute(f'SELECT * FROM {TABLE.FUNDS} WHERE {FUND.ID} = {dAmortFund[FUND.ID.value]}')
            row = self.__cursor.fetchone()
            colsFund = [column[0] for column in self.__cursor.description]
            dFund = dict(zip(colsFund, row))

            dJoin = dFund | dAmortFund

            dJoin[FUND.INI.value] = dJoin[FUND.INI.value].date()
            dJoin[FUND.VENC.value] = dJoin[FUND.VENC.value].date()
            dJoin[AMORT_FUND.DATA.value] = dJoin[AMORT_FUND.DATA.value].date()
            amortFunds.append(AmortFund.fromDict(dJoin))

        return amortFunds

    def getAllAmortDesembs(self) -> List[AmortDesemb]:
        self.__cursor.execute(f'SELECT * FROM {TABLE.AMORT_DESEMBS.value}')

        amortDesembs = []
        rows = self.__cursor.fetchall()
        colsAmortDesemb = [column[0] for column in self.__cursor.description]
        for amortDesemb in rows:
            dAmortDesemb = dict(zip(colsAmortDesemb, amortDesemb))

            # Fetching Desemb
            self.__cursor.execute(f'SELECT * FROM {TABLE.DESEMBS} WHERE {DESEMB.ID} = {dAmortDesemb[DESEMB.ID.value]}')
            rowDesemb = self.__cursor.fetchone()
            colsDesemb = [column[0] for column in self.__cursor.description]
            dDesemb = dict(zip(colsDesemb, rowDesemb))

            # Fetching Fund
            self.__cursor.execute(f'SELECT * FROM {TABLE.FUNDS} WHERE {FUND.ID} = {dDesemb[FUND.ID.value]}')
            rowFund = self.__cursor.fetchone()
            colsFund = [column[0] for column in self.__cursor.description]
            dFund = dict(zip(colsFund, rowFund))

            dJoin = dFund | dDesemb | dAmortDesemb

            dJoin[FUND.INI.value] = dJoin[FUND.INI.value].date()
            dJoin[FUND.VENC.value] = dJoin[FUND.VENC.value].date()
            dJoin[DESEMB.INI.value] = dJoin[DESEMB.INI.value].date()
            dJoin[DESEMB.VENC.value] = dJoin[DESEMB.VENC.value].date()
            dJoin[AMORT_DESEMB.DATA.value] = dJoin[AMORT_DESEMB.DATA.value].date()
            amortDesembs.append(AmortDesemb.fromDict(dJoin))

        return amortDesembs

    def getDesembsInFundByKold(self, kold: str) -> List[Desemb]:
        self.__cursor.execute(
            f'SELECT * '
            f'FROM {TABLE.DESEMBS} INNER JOIN {TABLE.FUNDS} '
            f'ON {TABLE.FUNDS}.{FUND.ID} = {TABLE.DESEMBS}.{DESEMB.FUND_ID} '
            f'WHERE {TABLE.FUNDS}.{FUND.KOLD} = \'{kold}\' '
            f'ORDER BY {TABLE.FUNDS}.{FUND.VENC}'
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
        return Fund.fromDict(d)

    def getFundByKold(self, kold: str) -> Fund:
        self.__cursor.execute(f'SELECT * FROM {TABLE.FUNDS} WHERE {FUND.KOLD} = \'{kold}\'')
        columns = [column[0] for column in self.__cursor.description]
        d = dict(zip(columns, self.__cursor.fetchone()))
        d[FUND.INI.value] = d[FUND.INI.value].date()
        d[FUND.VENC.value] = d[FUND.VENC.value].date()
        return Fund.fromDict(d)

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

        return Desemb.fromDict(dJoin)

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

        return AmortFund.fromDict(dJoin)

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

        return retAmortFunds

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

        return AmortDesemb.fromDict(dJoin)

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

            lAmortDesembs.append(dJoin)

        retAmortDesembs = []
        for amort in lAmortDesembs:
            retAmortDesembs.append(AmortDesemb.fromDict(amort))

        return retAmortDesembs

    def getRemainPrincInFundById(self, dealId: int) -> float:
        today = date.today()
        fund = self.getFundById(dealId)

        remain = fund.princ

        amorts = self.getAmortFundsByFundId(dealId)
        amorts.sort(key=lambda amort: amort.data)

        for amort in amorts:
            if amort.data < today:
                remain -= amort.val

        return remain
