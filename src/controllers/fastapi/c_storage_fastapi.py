import json
import os

from fastapi import FastAPI

from src.controllers.fastapi.enums.config import *
from src.controllers.fastapi.router.router import Router
from src.interfaces.i_c_storage import ICStorage
from src.usecases.uc_cash_flows import *
from src.usecases.uc_change_fund import *
from src.usecases.uc_get_all import *
from src.usecases.uc_get_desembs_in_fund import *
from src.usecases.uc_get_op_by_attr import *
from src.usecases.uc_get_values import *


class CStorageFastAPI(ICStorage):
    __storage: IStorage
    protocol: str
    host: str
    port: str
    url: str
    app: FastAPI

    def __init__(self, storage: IStorage, adapters: dict = dict({})):
        with open(os.path.join(os.path.dirname(__file__), 'config.json')) as file:
            data = json.load(file)
        self.__storage = storage
        self.protocol = data[CONFIG.PROTOCOL.value]
        self.host = data[CONFIG.HOST.value]
        self.port = data[CONFIG.PORT.value]
        self.url = f'{self.protocol}://{self.host}:{self.port}'
        self.app = FastAPI()
        self.app.include_router(Router(storage, self, adapters))

    def getAllFunds(self):
        return UCGetAllFunds(self.__storage)()

    def getAllDesembs(self):
        return UCGetAllDesembs(self.__storage)()

    def getAllAmortFunds(self):
        return UCGetAllAmortFunds(self.__storage)()

    def getAllAmortDesembs(self):
        return UCGetAllAmortDesembs(self.__storage)()

    def getDesembsInFundByKold(self, kold: str):
        return UCGetDesembsInFundByKold(self.__storage)(kold)

    def getFundById(self, dealId: int):
        return UCGetFundById(self.__storage)(dealId)

    def getFundByKold(self, kold: str):
        return UCGetFundByKold(self.__storage)(kold)

    def getDesembById(self, dealId: int):
        return UCGetDesembById(self.__storage)(dealId)

    def getDesembByCcb(self, ccb: str):
        return UCGetDesembByCcb(self.__storage)(ccb)

    def getAmortFundById(self, amortId: int):
        return UCGetAmortFundById(self.__storage)(amortId)

    def getAmortFundsByFundId(self, dealId: int):
        return UCGetAmortFundsByFundId(self.__storage)(dealId)

    def getAmortDesembById(self, amortId: int):
        return UCGetAmortDesembById(self.__storage)(amortId)

    def getAmortDesembsByDesembId(self, dealId: int):
        return UCGetAmortDesembsByDesembId(self.__storage)(dealId)

    def getFundPrincAfterAmortById(self, dealId: int, basedate: date = date.today()):
        return UCGetFundPrincAfterAmortById(self.__storage)(dealId, basedate)

    def getDesembPrincAfterAmortById(self, dealId: int, basedate: date = date.today()):
        return UCGetDesembPrincAfterAmortById(self.__storage)(dealId, basedate=basedate)

    def getAvailableFundsForDesembByCcb(self, ccb: str, basedate: date = date.today()):
        return UCgetAvailableFundsForDesembByCcb(self.__storage)(ccb, basedate=basedate)

    def generateFundFlowByKold(self, kold: str):
        return UCGenerateFundFlowByKold(self.__storage)(kold)

    def generateFundAvailabilityByKold(self, kold: str):
        return UCGenerateFundAvailabilityByKold(self.__storage)(kold)

    def changeFund(self, desemb: Desemb, newFund: Fund, override=False):
        return UCChangeFund(self.__storage)(desemb, newFund, override)
