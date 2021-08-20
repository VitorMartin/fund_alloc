import json
import os
from datetime import date

from fastapi import FastAPI

from src.controllers.excel.enums.config import CONFIG
from src.controllers.fastapi.c_storage_fastapi import CStorageFastAPI
from src.controllers.fastapi.http import *
from src.interfaces.i_storage import IStorage
from src.models.enums.dict_keys import *


class CStorageExcel(CStorageFastAPI):
    """
    Basically flattens all HttpResponse dicts from CStorageFastAPI before each method call.
    This must be used in conjunction with FastAPI implementation.
    This controller only exists because Excel is a pain in the ___ when dealing with complex JSONs and dicts.
    """
    def __init__(self, storage: IStorage):
        super().__init__(storage)

        with open(os.path.join(os.path.dirname(__file__), 'config.json')) as file:
            data = json.load(file)

        self.__storage = storage
        self.protocol = data[CONFIG.PROTOCOL.value]
        self.host = data[CONFIG.HOST.value]
        self.port = data[CONFIG.PORT.value]
        self.url = f'{self.protocol}://{self.host}:{self.port}'
        self.app = FastAPI()
        pass

    def getAllFunds(self) -> HttpResponse:
        newDict = {}
        httpRes = super().getAllFunds()
        funds = httpRes.body[MODEL.FUND]

        i = 0
        numColumns = 0
        while i < len(funds):
            fund = funds[i]
            for k, v in fund.items():
                newDict[f'{k}_{i}'] = str(v)
                if i == 0:
                    numColumns += 1
            i += 1

        httpRes.body = newDict
        httpRes.body['length'] = str(i)
        httpRes.body['num_columns'] = str(numColumns)

        return httpRes

    def getAllDesembs(self) -> HttpResponse:
        newDict = {}
        httpRes = super().getAllDesembs()
        desembs = httpRes.body[MODEL.DESEMB]
        i = 0
        numColumns = 0
        while i < len(desembs):
            desemb = desembs[i]
            for kd, vd in desemb.items():
                if kd == MODEL.FUND:
                    for kf, vf in desemb[MODEL.FUND].items():
                        newDict[f'{kf}_{i}'] = vf
                        if i == 0:
                            numColumns += 1
                else:
                    newDict[f'{kd}_{i}'] = vd
                    if i == 0:
                        numColumns += 1
            i += 1

        httpRes.body = newDict
        httpRes.body['length'] = str(i)
        httpRes.body['num_columns'] = str(numColumns)

        return httpRes

    def getAllAmortFunds(self) -> HttpResponse:
        return super().getAllAmortFunds()

    def getAllAmortDesembs(self) -> HttpResponse:
        return super().getAllAmortDesembs()

    def getDesembsInFundByKold(self, kold: str) -> HttpResponse:
        return super().getDesembsInFundByKold(kold)

    def getFundById(self, dealId: int) -> HttpResponse:
        return super().getFundById(dealId)

    def getFundByKold(self, kold: str) -> HttpResponse:
        return super().getFundByKold(kold)

    def getDesembById(self, dealId: int) -> HttpResponse:
        return super().getDesembById(dealId)

    def getDesembByCcb(self, ccb: str) -> HttpResponse:
        return super().getDesembByCcb(ccb)

    def getAmortFundById(self, amortId: int) -> HttpResponse:
        return super().getAmortFundById(amortId)

    def getAmortFundsByFundId(self, dealId: int) -> HttpResponse:
        return super().getAmortFundsByFundId(dealId)

    def getAmortDesembById(self, amortId: int) -> HttpResponse:
        return super().getAmortDesembById(amortId)

    def getAmortDesembsByDesembId(self, dealId: int) -> HttpResponse:
        return super().getAmortDesembsByDesembId(dealId)

    def getFundPrincAfterAmortById(self, dealId: int, basedate: date = date.today()) -> HttpResponse:
        return super().getFundPrincAfterAmortById(dealId, basedate)

    def getDesembPrincAfterAmortById(self, dealId: int, basedate: date = date.today()) -> HttpResponse:
        return super().getDesembPrincAfterAmortById(dealId, basedate)

    def getAvailableFundsForDesembByCcb(self, ccb: str, basedate: date = date.today()) -> HttpResponse:
        return super().getAvailableFundsForDesembByCcb(ccb, basedate)

    def generateAmortsInFundByKold(self, kold: str) -> HttpResponse:
        return super().generateAmortsInFundByKold(kold)

    def generateFundAvailByKold(self, kold: str) -> HttpResponse:
        return super().generateFundAvailByKold(kold)
