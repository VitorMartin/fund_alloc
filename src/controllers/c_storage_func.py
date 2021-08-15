from src.interfaces.i_c_storage import ICStorage
from src.usecases.uc_get_all import *
from src.usecases.uc_get_desembs_in_fund import *
from src.usecases.uc_get_op_by_attr import *
from src.usecases.uc_get_values import *


class CStorageFunc(ICStorage):
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

    def getFundByKold(self, kold: str) -> Fund:
        return UCGetFundByKold(self.storage)(kold)

    def getDesembById(self, dealId: int) -> Desemb:
        return UCGetDesembById(self.storage)(dealId)

    def getDesembByCcb(self, ccb: str) -> Desemb:
        return UCGetDesembByCcb(self.storage)(ccb)

    def getAmortFundById(self, amortId: int) -> AmortFund:
        return UCGetAmortFundById(self.storage)(amortId)

    def getAmortFundsByFundId(self, dealId: int) -> List[AmortFund]:
        return UCGetAmortFundsByFundId(self.storage)(dealId)

    def getAmortDesembById(self, amortId: int) -> AmortDesemb:
        return UCGetAmortDesembById(self.storage)(amortId)

    def getAmortDesembsByDesembId(self, dealId: int) -> List[AmortDesemb]:
        return UCGetAmortDesembsByDesembId(self.storage)(dealId)

    def getFundPrincAfterAmortById(self, dealId: int, basedate: date = date.today()) -> float:
        return UCgetRemainPrincInFundById(self.storage)(dealId, basedate)

    def getDesembPrincAfterAmortById(self, dealId: int, basedate: date = date.today()) -> float:
        return UCgetRemainPrincInDesembById(self.storage)(dealId, basedate=basedate)
