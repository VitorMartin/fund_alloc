from typing import List

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
        pass

    def getFundById(self, dealId: int) -> Fund:
        pass

    def getDesembById(self, dealId: int) -> Desemb:
        pass

    def getAmortFundById(self, amortId: int) -> AmortFund:
        pass

    def getAmortDesembById(self, amortId: int) -> AmortDesemb:
        pass
