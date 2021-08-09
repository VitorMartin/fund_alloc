from abc import ABC, abstractmethod
from typing import List

from src.models.amort_desemb import AmortDesemb
from src.models.amort_fund import AmortFund
from src.models.desemb import Desemb
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
