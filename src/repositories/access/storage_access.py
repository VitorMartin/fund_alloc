import os
from datetime import date
from typing import Any, List

import pyodbc

from src.interfaces.i_storage import IStorage
from src.models.amort import Amort
from src.models.amort_desemb import AmortDesemb
from src.models.amort_fund import AmortFund
from src.models.desemb import Desemb
from src.models.enums.ccy import CCY
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
        self.__dbPath = os.path.dirname(__file__)
        self.__connectionStr = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=' + os.path.join(self.__dbPath, self.__dbFilename)
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
            self.__cursor.execute(f'SELECT * FROM {TABLE.FUNDS} WHERE {FUND.ID} = {dDesemb[DESEMB.FUND_ID.value]}')
            fundColumns = [column[0] for column in self.__cursor.description]
            dFund = dict(zip(fundColumns, self.__cursor.fetchone()))
            dJoin = dFund | dDesemb

            dJoin[FUND.INI.value] = dJoin[FUND.INI.value].date()
            dJoin[FUND.VENC.value] = dJoin[FUND.VENC.value].date()
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
            self.__cursor.execute(
                f'SELECT * FROM {TABLE.FUNDS} '
                f'WHERE {DESEMB.FUND_ID} = {dDesemb[DESEMB.FUND_ID.value]}'
            )
            fundColumns = [column[0] for column in self.__cursor.description]
            dFund = dict(zip(fundColumns, self.__cursor.fetchone()))
            dJoin = dFund | dDesemb | dAmortDesemb

            dJoin[FUND.INI.value] = dJoin[FUND.INI.value].date()
            dJoin[FUND.VENC.value] = dJoin[FUND.VENC.value].date()
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

    def getDesembByCcb(self, ccb: str) -> Desemb:
        # Fetching desemb
        self.__cursor.execute(f'SELECT * FROM {TABLE.DESEMBS} WHERE {DESEMB.CCB} = \'{ccb}\'')
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

    def getFundPrincAfterAmortById(self, dealId: int, basedate: date = date.today()) -> float:
        fund = self.getFundById(dealId)

        remain = fund.princ

        amorts = self.getAmortFundsByFundId(dealId)
        amorts.sort(key=lambda amort: amort.data)

        for amort in amorts:
            if amort.data < basedate:
                remain -= amort.val

        return remain

    def getDesembPrincAfterAmortById(self, dealId: int, basedate: date = date.today()) -> float:
        desemb = self.getDesembById(dealId)

        remain = desemb.princ

        amorts = self.getAmortDesembsByDesembId(dealId)
        amorts.sort(key=lambda amort: amort.data)

        for amort in amorts:
            if amort.data < basedate:
                remain -= amort.val

        return remain

    def getAvailableFundsForDesembByCcb(self, ccb: str, basedate: date = date.today()) -> List[Fund]:
        desemb = self.getDesembByCcb(ccb)
        allFunds = self.getAllFunds()
        availFunds = []

        for fund in allFunds:
            fundAvailability = self.getFundPrincAfterAmortById(fund.dealId, basedate=basedate)
            if fund.ccy == desemb.ccy and fundAvailability > desemb.princ:
                availFunds.append(fund)

        return availFunds

    def generateFundFlowByKold(self, kold: str) -> List[Amort]:
        fund = self.getFundByKold(kold)
        self.__cursor.execute(f'SELECT * FROM {TABLE.AMORT_FUNDS} WHERE {AMORT_FUND.FUND_ID} = {fund.dealId}')
        flow = []
        for row in self.__cursor.fetchall():
            flow.append(self.parseRow(MODEL.AMORT_FUND, row))
        desembs = self.getDesembsInFundByKold(kold)
        for desemb in desembs:
            amortDesembs = self.getAmortDesembsByDesembId(desemb.dealId)
            [flow.append(amortDesemb) for amortDesemb in amortDesembs]

        flow.sort(key=lambda movement: movement.data)

        return flow

    def generateFundAvailByKold(self, kold: str) -> List[dict[Any, str, date, float, float, float, float, float]]:
        def movementConstructor(_op, _opType, _opData, _opVal, _fundPrinc, _desembPrinc, _availBefore, _availAfter):
            return {
                MOVEMENT.OP.value: _op,
                MOVEMENT.TYPE.value: _opType,
                MOVEMENT.DATA.value: _opData,
                MOVEMENT.VAL.value: _opVal,
                MOVEMENT.FUND_PRINC.value: _fundPrinc,
                MOVEMENT.DESEMB_PRINC.value: _desembPrinc,
                MOVEMENT.AVAIL_BEFORE.value: _availBefore,
                MOVEMENT.AVAIL_AFTER.value: _availAfter
            }

        flow = []

        # Initial funding
        fund = self.getFundByKold(kold)
        flow.append(
            movementConstructor(fund, MODEL.FUND.value, fund.ini, fund.princ, 0, 0, 0, 0)
        )

        # All desembs
        desembs = self.getDesembsInFundByKold(kold)
        for desemb in desembs:
            flow.append(
                movementConstructor(desemb, MODEL.DESEMB.value, desemb.ini, desemb.princ, 0, 0, 0, 0)
            )

        # All amorts
        amorts = self.generateFundFlowByKold(kold)
        for amort in amorts:
            if amort.__class__.__name__ == AmortFund.__name__:
                amortType = MODEL.AMORT_FUND.value
            elif amort.__class__.__name__ == AmortDesemb.__name__:
                amortType = MODEL.AMORT_DESEMB.value
            else:
                amortType = MODEL.AMORT.value

            flow.append(
                movementConstructor(amort, amortType, amort.data, amort.val, 0, 0, 0, 0)
            )

        flow.sort(key=lambda movement: movement[MOVEMENT.DATA.value])

        for i in range(len(flow)):
            if i == 0:
                prevMovement = movementConstructor(
                    Amort(date(2000, 1, 1), CCY.USD, 0., pk=-1), '', date(2000, 1, 1), 0., 0., 0., 0., 0.
                )
            else:
                prevMovement = flow[i-1]

            movement = flow[i]
            op = movement[MOVEMENT.OP.value]

            if movement[MOVEMENT.TYPE.value] == MODEL.FUND.value:
                movement[MOVEMENT.FUND_PRINC.value] += op.princ
                movement[MOVEMENT.DESEMB_PRINC.value] += prevMovement[MOVEMENT.DESEMB_PRINC.value]
                movement[MOVEMENT.AVAIL_BEFORE.value] = prevMovement[MOVEMENT.AVAIL_AFTER.value]
                movement[MOVEMENT.AVAIL_AFTER.value] = \
                    movement[MOVEMENT.AVAIL_BEFORE.value] + movement[MOVEMENT.VAL.value]

            elif movement[MOVEMENT.TYPE.value] == MODEL.DESEMB.value:
                movement[MOVEMENT.FUND_PRINC.value] += prevMovement[MOVEMENT.FUND_PRINC.value]
                movement[MOVEMENT.DESEMB_PRINC.value] += op.princ
                movement[MOVEMENT.AVAIL_BEFORE.value] = prevMovement[MOVEMENT.AVAIL_AFTER.value]
                movement[MOVEMENT.AVAIL_AFTER.value] = \
                    movement[MOVEMENT.AVAIL_BEFORE.value] - movement[MOVEMENT.VAL.value]

            elif movement[MOVEMENT.TYPE.value] == MODEL.AMORT_FUND.value:
                movement[MOVEMENT.FUND_PRINC.value] += prevMovement[MOVEMENT.FUND_PRINC.value]
                movement[MOVEMENT.DESEMB_PRINC.value] += prevMovement[MOVEMENT.DESEMB_PRINC.value]
                movement[MOVEMENT.AVAIL_BEFORE.value] = prevMovement[MOVEMENT.AVAIL_AFTER.value]
                movement[MOVEMENT.AVAIL_AFTER.value] = \
                    movement[MOVEMENT.AVAIL_BEFORE.value] - movement[MOVEMENT.VAL.value]

            elif movement[MOVEMENT.TYPE.value] == MODEL.AMORT_DESEMB.value:
                movement[MOVEMENT.FUND_PRINC.value] += prevMovement[MOVEMENT.FUND_PRINC.value]
                movement[MOVEMENT.DESEMB_PRINC.value] += prevMovement[MOVEMENT.DESEMB_PRINC.value]
                movement[MOVEMENT.AVAIL_BEFORE.value] = prevMovement[MOVEMENT.AVAIL_AFTER.value]
                movement[MOVEMENT.AVAIL_AFTER.value] = \
                    movement[MOVEMENT.AVAIL_BEFORE.value] + movement[MOVEMENT.VAL.value]

        return flow
