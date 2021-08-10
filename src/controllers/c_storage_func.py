from src.usecases.uc_get_all import *
from src.usecases.uc_get_desembs_in_fund import *
from src.usecases.uc_get_op_by_attr import *


class CStorageFunc:
    __storage: IStorage

    def __init__(self, storage: IStorage):
        self.storage = storage

    def getAllFunds(self) -> List[Fund]:
        return UCGetAllFunds(self.storage)()

    def getAllDesembs(self) -> List[Desemb]:
        return UCGetAllDesembs(self.storage)()

    def getAllAmortFunds(self) -> List[AmortFund]:
        return UCGetAllAmortFunds(self.storage)()

    def getAllAmortDesembs(self) -> List[AmortDesemb]:
        return UCGetAllAmortDesembs(self.storage)()

    def getDesembsInFundByKold(self, kold: str) -> List[Desemb]:
        return UCGetDesembsInFundByKold(self.storage)(kold)

    def getFundById(self, dealId: int) -> Fund:
        return UCGetFundById(self.storage)(dealId)

    def getDesembById(self, dealId: int) -> Desemb:
        return UCGetDesembById(self.storage)(dealId)

    def getAmortFundById(self, amortId: int) -> AmortFund:
        return UCGetAmortFundById(self.storage)(amortId)

    def getAmortDesembById(self, amortId: int) -> AmortDesemb:
        return UCGetAmortDesembById(self.storage)(amortId)
