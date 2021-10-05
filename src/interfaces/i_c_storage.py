from abc import ABC, abstractmethod
from datetime import date
from typing import Any, List

from src.models.amort import Amort
from src.models.amort_desemb import AmortDesemb
from src.models.amort_fund import AmortFund
from src.models.desemb import Desemb
from src.models.fund import Fund


class ICStorage(ABC):
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

    @abstractmethod
    def getFundPrincAfterAmortById(self, dealId: int, basedate: date = date.today()) -> float:
        pass

    @abstractmethod
    def getDesembPrincAfterAmortById(self, dealId: int, basedate: date = date.today()) -> float:
        pass

    @abstractmethod
    def getAvailableFundsForDesembByCcb(self, ccb: str, basedate: date = date.today()) -> List[Fund]:
        pass

    @abstractmethod
    def generateFundFlowByKold(self, kold: str) -> List[Amort]:
        pass

    @abstractmethod
    def generateFundAvailabilityByKold(self, kold: str) \
            -> List[dict[Any, str, date, float, float, float, float, float]]:
        pass

    @abstractmethod
    def changeFund(self, desemb: Desemb, newFund: Fund) -> bool:
        pass
