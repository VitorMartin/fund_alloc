from src.interfaces.i_c_storage import ICStorage
from src.usecases.uc_cash_flows import *
from src.usecases.uc_change_fund import *
from src.usecases.uc_get_all import *
from src.usecases.uc_get_desembs_in_fund import *
from src.usecases.uc_get_op_by_attr import *
from src.usecases.uc_get_values import *


class CStorageFunc(ICStorage):
    __storage: IStorage

    def __init__(self, storage: IStorage):
        self.__storage = storage

    def getAllFunds(self) -> List[Fund]:
        return UCGetAllFunds(self.__storage)()

    def getAllDesembs(self) -> List[Desemb]:
        return UCGetAllDesembs(self.__storage)()

    def getAllAmortFunds(self) -> List[AmortFund]:
        return UCGetAllAmortFunds(self.__storage)()

    def getAllAmortDesembs(self) -> List[AmortDesemb]:
        return UCGetAllAmortDesembs(self.__storage)()

    def getDesembsInFundByKold(self, kold: str) -> List[Desemb]:
        return UCGetDesembsInFundByKold(self.__storage)(kold)

    def getFundById(self, dealId: int) -> Fund:
        return UCGetFundById(self.__storage)(dealId)

    def getFundByKold(self, kold: str) -> Fund:
        return UCGetFundByKold(self.__storage)(kold)

    def getDesembById(self, dealId: int) -> Desemb:
        return UCGetDesembById(self.__storage)(dealId)

    def getDesembByCcb(self, ccb: str) -> Desemb:
        return UCGetDesembByCcb(self.__storage)(ccb)

    def getAmortFundById(self, amortId: int) -> AmortFund:
        return UCGetAmortFundById(self.__storage)(amortId)

    def getAmortFundsByFundId(self, dealId: int) -> List[AmortFund]:
        return UCGetAmortFundsByFundId(self.__storage)(dealId)

    def getAmortDesembById(self, amortId: int) -> AmortDesemb:
        return UCGetAmortDesembById(self.__storage)(amortId)

    def getAmortDesembsByDesembId(self, dealId: int) -> List[AmortDesemb]:
        return UCGetAmortDesembsByDesembId(self.__storage)(dealId)

    def getFundPrincAfterAmortById(self, dealId: int, basedate: date = date.today()) -> float:
        return UCGetFundPrincAfterAmortById(self.__storage)(dealId, basedate)

    def getDesembPrincAfterAmortById(self, dealId: int, basedate: date = date.today()) -> float:
        return UCGetDesembPrincAfterAmortById(self.__storage)(dealId, basedate=basedate)

    def getAvailableFundsForDesembByCcb(self, ccb: str, basedate: date = date.today()) -> List[Fund]:
        return UCgetAvailableFundsForDesembByCcb(self.__storage)(ccb, basedate=basedate)

    def generateFundFlowByKold(self, kold: str) -> List[Amort]:
        return UCGenerateFundFlowByKold(self.__storage)(kold)

    def generateFundAvailabilityByKold(self, kold: str) \
            -> List[dict[Any, str, date, float, float, float, float, float]]:
        return UCGenerateFundAvailabilityByKold(self.__storage)(kold)

    def changeFund(self, desemb: Desemb, newFund: Fund):
        return UCChangeFund(self.__storage)(desemb, newFund)
