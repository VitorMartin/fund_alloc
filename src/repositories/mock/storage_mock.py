from typing import List

from repositories.errors.repository_error import NotFoundError
from src.interfaces.i_storage import IStorage
from src.models.amort_desemb import AmortDesemb
from src.models.amort_fund import AmortFund
from src.models.desemb import Desemb
from src.models.fund import Fund
from src.repositories.mock.mock_data import MockData


class StorageMock(IStorage):
    __funds: list[Fund]
    __desembs: list[Desemb]
    __amortFunds: list[AmortFund]
    __amortDesembs: list[AmortDesemb]

    def __init__(
            self, funds: list[Fund] = MockData.funds, desembs: list[Desemb] = MockData.desembs,
            amortFunds: list[AmortFund] = MockData.amortFunds, amortDesembs: list[AmortDesemb] = MockData.amortDesembs
    ):
        self.__funds = funds
        self.__desembs = desembs
        self.__amortFunds = amortFunds
        self.__amortDesembs = amortDesembs

    def getAllFunds(self) -> List[Fund]:
        return self.__funds

    def getAllDesembs(self) -> List[Desemb]:
        return self.__desembs

    def getAllAmortFunds(self) -> List[AmortFund]:
        return self.__amortFunds

    def getAllAmortDesembs(self) -> List[AmortDesemb]:
        return self.__amortDesembs

    def getDesembsInFundByKold(self, kold: str) -> List[Desemb]:
        return [desemb for desemb in self.__desembs if desemb.fund.kold == kold]

    def getFundById(self, dealId: int) -> Fund:
        fundsFound = [fund for fund in self.__funds if fund.dealId == dealId]
        try:
            return fundsFound[0]
        except IndexError:
            raise NotFoundError()

    def getFundByKold(self, kold: str) -> Fund:
        fundsFound = [fund for fund in self.__funds if fund.kold == kold]
        try:
            return fundsFound[0]
        except IndexError:
            raise NotFoundError()

    def getDesembById(self, dealId: int) -> Desemb:
        desembsFound = [desemb for desemb in self.__desembs if desemb.dealId == dealId]
        try:
            return desembsFound[0]
        except IndexError:
            raise NotFoundError()

    def getDesembByCcb(self, ccb: str) -> Desemb:
        desembsFound = [desemb for desemb in self.__desembs if desemb.ccb == ccb]
        try:
            return desembsFound[0]
        except IndexError:
            raise NotFoundError()

    def getAmortFundById(self, amortId: int) -> AmortFund:
        amortFundsFound = [amortFund for amortFund in self.__amortFunds if amortFund.amortId == amortId]
        try:
            return amortFundsFound[0]
        except IndexError:
            raise NotFoundError()

    def getAmortFundsByFundId(self, dealId: int) -> List[AmortFund]:
        return [amortFund for amortFund in self.__amortFunds if amortFund.fund.dealId == dealId]

    def getAmortDesembById(self, amortId: int) -> AmortDesemb:
        amortDesembsFound = [amortDesemb for amortDesemb in self.__amortDesembs if amortDesemb.amortId == amortId]
        try:
            return amortDesembsFound[0]
        except IndexError:
            raise NotFoundError()

    def getAmortDesembsByDesembId(self, dealId: int) -> List[AmortDesemb]:
        return [amortDesemb for amortDesemb in self.__amortDesembs if amortDesemb.desemb.dealId == dealId]

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
        index = self.__desembs.index(desemb)
        desemb.fund = newFund
        try:
            self.__desembs[index] = desemb
            return True
        except IndexError:
            return False
