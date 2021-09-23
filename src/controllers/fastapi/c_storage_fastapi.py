import json
import os

from fastapi import FastAPI

from src.controllers.fastapi.enums.config import *
from src.controllers.fastapi.http.models import *
from src.controllers.fastapi.http.responses import *
from src.interfaces.i_c_storage import ICStorage
from src.usecases.uc_get_all import *
from src.usecases.uc_get_values import *


class CStorageFastAPI(ICStorage):
    __storage: IStorage
    protocol: str
    host: str
    port: str
    url: str
    app: FastAPI

    def __init__(self, storage: IStorage):
        with open(os.path.join(os.path.dirname(__file__), 'config.json')) as file:
            data = json.load(file)
        self.__storage = storage
        self.protocol = data[CONFIG.PROTOCOL.value]
        self.host = data[CONFIG.HOST.value]
        self.port = data[CONFIG.PORT.value]
        self.url = f'{self.protocol}://{self.host}:{self.port}'
        self.app = FastAPI()

    def getAllFunds(self) -> List[FundModel]:
        fundModels = []
        funds = UCGetAllFunds(self.__storage)()
        for fund in funds:
            fundModels.append(fund.toModel())
        return fundModels

    def getAllDesembs(self) -> List[DesembModel]:
        desembModels = []
        desembs = UCGetAllDesembs(self.__storage)()
        for desemb in desembs:
            desembModels.append(desemb.toModel())
        return desembModels

    def getAllAmortFunds(self) -> List[AmortFundModel]:
        pass

    def getAllAmortDesembs(self) -> List[AmortDesembModel]:
        pass

    def getDesembsInFundByKold(self, kold: str) -> List[DesembModel]:
        pass

    def getFundById(self, dealId: int) -> FundModel:
        pass

    def getFundByKold(self, kold: str) -> FundModel:
        pass

    def getDesembById(self, dealId: int) -> DesembModel:
        pass

    def getDesembByCcb(self, ccb: str) -> DesembModel:
        pass

    def getAmortFundById(self, amortId: int) -> AmortFundModel:
        pass

    def getAmortFundsByFundId(self, dealId: int) -> AmortFundModel:
        pass

    def getAmortDesembById(self, amortId: int) -> AmortDesembModel:
        pass

    def getAmortDesembsByDesembId(self, dealId: int) -> AmortDesembModel:
        pass

    def getFundPrincAfterAmortById(self, dealId: int, basedate: date = date.today()) -> ValueModel:
        pass

    def getDesembPrincAfterAmortById(self, dealId: int, basedate: date = date.today()) -> ValueModel:
        pass

    def getAvailableFundsForDesembByCcb(self, ccb: str, basedate: date = date.today()) -> List[FundModel]:
        pass

    def generateAmortsInFundByKold(self, kold: str) -> List[AmortModel]:
        pass

    def generateFundAvailByKold(self, kold: str) -> List[dict]:
        pass
