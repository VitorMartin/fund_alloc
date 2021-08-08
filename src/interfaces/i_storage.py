from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def getAllFunds(self):
        pass

    @abstractmethod
    def getAllDesembs(self):
        pass

    @abstractmethod
    def getAllAmortFunds(self):
        pass

    @abstractmethod
    def getAllAmortDesembs(self):
        pass

    @abstractmethod
    def getDesembsInFundByKold(self, kold: str):
        pass
