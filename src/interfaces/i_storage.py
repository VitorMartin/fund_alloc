from abc import ABC, abstractmethod
from datetime import date
from typing import List, Union

from src.models.amort import Amort
from src.models.amort_desemb import AmortDesemb
from src.models.amort_fund import AmortFund
from src.models.desemb import Desemb
from src.models.enums.ccy import CCY
from src.models.enums.dict_keys import FLOW_CHANGE, MODEL
from src.models.fund import Fund


class IStorage(ABC):
    @abstractmethod
    def getAllFunds(self) -> List[Fund]:
        pass

    @abstractmethod
    def getAllDesembs(self) -> List[Desemb]:
        pass

    @abstractmethod
    def getAllAmortFunds(self) -> List[AmortFund]:
        pass

    @abstractmethod
    def getAllAmortDesembs(self) -> List[AmortDesemb]:
        pass

    @abstractmethod
    def getDesembsInFundByKold(self, kold: str) -> List[Desemb]:
        pass

    @abstractmethod
    def getFundById(self, dealId: int) -> Fund:
        pass

    @abstractmethod
    def getFundByKold(self, kold: str) -> Fund:
        pass

    @abstractmethod
    def getDesembById(self, dealId: int) -> Desemb:
        pass

    @abstractmethod
    def getDesembByCcb(self, ccb: str) -> Desemb:
        pass

    @abstractmethod
    def getAmortFundById(self, amortId: int) -> AmortFund:
        pass

    @abstractmethod
    def getAmortFundsByFundId(self, dealId: int) -> List[AmortFund]:
        pass

    @abstractmethod
    def getAmortDesembById(self, amortId: int) -> AmortDesemb:
        pass

    @abstractmethod
    def getAmortDesembsByDesembId(self, dealId: int) -> List[AmortDesemb]:
        pass

    def getFundPrincAfterAmortById(self, dealId: int, basedate: date = date.today()) -> float:
        fund = self.getFundById(dealId)

        remainingPrinc = fund.princ

        amorts = self.getAmortFundsByFundId(dealId)
        amorts.sort(key=lambda _amort: _amort.data)

        for amort in amorts:
            if amort.data < basedate:
                remainingPrinc -= amort.val

        return remainingPrinc

    def getDesembPrincAfterAmortById(self, dealId: int, basedate: date = date.today()) -> float:
        desemb = self.getDesembById(dealId)

        remain = desemb.princ

        amorts = self.getAmortDesembsByDesembId(dealId)
        amorts.sort(key=lambda _amort: _amort.data)

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

    def getAmortsInFundByKold(self, kold: str) -> List[Amort]:
        fund = self.getFundByKold(kold)
        flow: List[Amort] = [amortFund for amortFund in self.getAllAmortFunds() if amortFund.fund.kold == fund.kold]
        desembs = self.getDesembsInFundByKold(kold)
        for desemb in desembs:
            amortDesembs = self.getAmortDesembsByDesembId(desemb.dealId)
            [flow.append(amortDesemb) for amortDesemb in amortDesembs]

        flow.sort(key=lambda movement: movement.data)

        return flow

    def generateFundFlowByKold(self, kold: str) -> List[dict[
        str, Union[Fund, Desemb, AmortFund, AmortDesemb, str, date, float]]
    ]:
        def flowChangeConstructor(_op, _opType, _opData, _opVal, _fundPrinc, _desembPrinc, _availBefore, _availAfter):
            return {
                FLOW_CHANGE.OP.value: _op,
                FLOW_CHANGE.TYPE.value: _opType,
                FLOW_CHANGE.DATA.value: _opData,
                FLOW_CHANGE.VAL.value: _opVal,
                FLOW_CHANGE.FUND_PRINC.value: _fundPrinc,
                FLOW_CHANGE.DESEMB_PRINC.value: _desembPrinc,
                FLOW_CHANGE.AVAIL_BEFORE.value: _availBefore,
                FLOW_CHANGE.AVAIL_AFTER.value: _availAfter
            }

        flow = []

        # Initial funding
        fund = self.getFundByKold(kold)
        flow.append(
            flowChangeConstructor(fund, MODEL.FUND.value, fund.ini, fund.princ, 0, 0, 0, 0)
        )

        # All desembs
        desembs = self.getDesembsInFundByKold(kold)
        for desemb in desembs:
            flow.append(
                flowChangeConstructor(desemb, MODEL.DESEMB.value, desemb.ini, desemb.princ, 0, 0, 0, 0)
            )

        # All amorts
        amorts = self.getAmortsInFundByKold(kold)
        for amort in amorts:
            if amort.__class__.__name__ == AmortFund.__name__:
                amortType = MODEL.AMORT_FUND.value
            elif amort.__class__.__name__ == AmortDesemb.__name__:
                amortType = MODEL.AMORT_DESEMB.value
            else:
                amortType = MODEL.AMORT.value

            flow.append(
                flowChangeConstructor(amort, amortType, amort.data, amort.val, 0, 0, 0, 0)
            )

        flow.sort(key=lambda _movement: _movement[FLOW_CHANGE.DATA.value])

        for i in range(len(flow)):
            if i == 0:
                prevMovement = flowChangeConstructor(
                    Amort(date(2000, 1, 1), CCY.USD, 0., pk=-1), '', date(2000, 1, 1), 0., 0., 0., 0., 0.
                )
            else:
                prevMovement = flow[i - 1]

            movement = flow[i]
            op = movement[FLOW_CHANGE.OP.value]

            if movement[FLOW_CHANGE.TYPE.value] == MODEL.FUND.value:
                movement[FLOW_CHANGE.FUND_PRINC.value] += op.princ
                movement[FLOW_CHANGE.DESEMB_PRINC.value] += prevMovement[FLOW_CHANGE.DESEMB_PRINC.value]
                movement[FLOW_CHANGE.AVAIL_BEFORE.value] = prevMovement[FLOW_CHANGE.AVAIL_AFTER.value]
                movement[FLOW_CHANGE.AVAIL_AFTER.value] = \
                    movement[FLOW_CHANGE.AVAIL_BEFORE.value] + movement[FLOW_CHANGE.VAL.value]

            elif movement[FLOW_CHANGE.TYPE.value] == MODEL.DESEMB.value:
                movement[FLOW_CHANGE.FUND_PRINC.value] += prevMovement[FLOW_CHANGE.FUND_PRINC.value]
                movement[FLOW_CHANGE.DESEMB_PRINC.value] += op.princ
                movement[FLOW_CHANGE.AVAIL_BEFORE.value] = prevMovement[FLOW_CHANGE.AVAIL_AFTER.value]
                movement[FLOW_CHANGE.AVAIL_AFTER.value] = \
                    movement[FLOW_CHANGE.AVAIL_BEFORE.value] - movement[FLOW_CHANGE.VAL.value]

            elif movement[FLOW_CHANGE.TYPE.value] == MODEL.AMORT_FUND.value:
                movement[FLOW_CHANGE.FUND_PRINC.value] += prevMovement[FLOW_CHANGE.FUND_PRINC.value]
                movement[FLOW_CHANGE.DESEMB_PRINC.value] += prevMovement[FLOW_CHANGE.DESEMB_PRINC.value]
                movement[FLOW_CHANGE.AVAIL_BEFORE.value] = prevMovement[FLOW_CHANGE.AVAIL_AFTER.value]
                movement[FLOW_CHANGE.AVAIL_AFTER.value] = \
                    movement[FLOW_CHANGE.AVAIL_BEFORE.value] - movement[FLOW_CHANGE.VAL.value]

            elif movement[FLOW_CHANGE.TYPE.value] == MODEL.AMORT_DESEMB.value:
                movement[FLOW_CHANGE.FUND_PRINC.value] += prevMovement[FLOW_CHANGE.FUND_PRINC.value]
                movement[FLOW_CHANGE.DESEMB_PRINC.value] += prevMovement[FLOW_CHANGE.DESEMB_PRINC.value]
                movement[FLOW_CHANGE.AVAIL_BEFORE.value] = prevMovement[FLOW_CHANGE.AVAIL_AFTER.value]
                movement[FLOW_CHANGE.AVAIL_AFTER.value] = \
                    movement[FLOW_CHANGE.AVAIL_BEFORE.value] + movement[FLOW_CHANGE.VAL.value]

        return flow

    @abstractmethod
    def changeFund(self, desemb: Desemb, newFund: Fund):
        pass

    @abstractmethod
    def createFund(self, fund: Fund, amorts: List[AmortFund]) -> Fund:
        pass

    @abstractmethod
    def createDesemb(self, desemb: Desemb, amorts: List[AmortDesemb]) -> Desemb:
        pass
