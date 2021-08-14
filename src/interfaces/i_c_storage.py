from abc import ABC
from typing import List

from src.models.amort_desemb import AmortDesemb
from src.models.amort_fund import AmortFund
from src.models.desemb import Desemb
from src.models.fund import Fund


class ICStorage(ABC):
    @staticmethod
    def getAllFunds(self) -> List[Fund]:
        pass

    @staticmethod
    def getAllDesembs(self) -> List[Desemb]:
        pass

    @staticmethod
    def getAllAmortFunds(self) -> List[AmortFund]:
        pass

    @staticmethod
    def getAllAmortDesembs(self) -> List[AmortDesemb]:
        pass

    @staticmethod
    def getDesembsInFundByKold(self, kold: str) -> List[Desemb]:
        pass

    @staticmethod
    def getFundById(self, dealId: int) -> Fund:
        pass

    @staticmethod
    def getFundByKold(self, dealId: int) -> Fund:
        pass

    @staticmethod
    def getDesembById(self, dealId: int) -> Desemb:
        pass

    @staticmethod
    def getAmortFundById(self, amortId: int) -> AmortFund:
        pass

    @staticmethod
    def getAmortFundsByFundId(self, dealId: int) -> List[AmortFund]:
        pass

    @staticmethod
    def getAmortDesembById(self, amortId: int) -> AmortDesemb:
        pass
