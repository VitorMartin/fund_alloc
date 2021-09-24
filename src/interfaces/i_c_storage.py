from abc import ABC, abstractmethod
from datetime import date
from typing import Any


class ICStorage(ABC):
    @abstractmethod
    def getAllFunds(self) -> Any:
        pass

    @abstractmethod
    def getAllDesembs(self) -> Any:
        pass

    @abstractmethod
    def getAllAmortFunds(self) -> Any:
        pass

    @abstractmethod
    def getAllAmortDesembs(self) -> Any:
        pass

    @abstractmethod
    def getDesembsInFundByKold(self, kold: str) -> Any:
        pass

    @abstractmethod
    def getFundById(self, dealId: int) -> Any:
        pass

    @abstractmethod
    def getFundByKold(self, kold: str) -> Any:
        pass

    @abstractmethod
    def getDesembById(self, dealId: int) -> Any:
        pass

    @abstractmethod
    def getDesembByCcb(self, ccb: str) -> Any:
        pass

    @abstractmethod
    def getAmortFundById(self, amortId: int) -> Any:
        pass

    @abstractmethod
    def getAmortFundsByFundId(self, dealId: int) -> Any:
        pass

    @abstractmethod
    def getAmortDesembById(self, amortId: int) -> Any:
        pass

    @abstractmethod
    def getAmortDesembsByDesembId(self, dealId: int) -> Any:
        pass

    @abstractmethod
    def getFundPrincAfterAmortById(self, dealId: int, basedate: date = date.today()) -> Any:
        pass

    @abstractmethod
    def getDesembPrincAfterAmortById(self, dealId: int, basedate: date = date.today()) -> Any:
        pass

    @abstractmethod
    def getAvailableFundsForDesembByCcb(self, ccb: str, basedate: date = date.today()) -> Any:
        pass

    @abstractmethod
    def generateFundFlowByKold(self, kold: str) -> Any:
        pass

    @abstractmethod
    def generateFundAvailByKold(self, kold: str) -> Any:
        pass
