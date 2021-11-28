import json
import os

import uvicorn
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

from src.controllers.fastapi.enums.config import *
from src.controllers.fastapi.router.router import Router
from src.interfaces.i_c_storage import ICStorage
from src.usecases.uc_cash_flows import *
from src.usecases.uc_change_fund import *
from src.usecases.uc_create_deals import *
from src.usecases.uc_get_all import *
from src.usecases.uc_get_desembs_in_fund import *
from src.usecases.uc_get_op_by_attr import *
from src.usecases.uc_get_op_by_attr import UCGetAmortsInFundByKold
from src.usecases.uc_get_values import *


class CStorageFastAPI(ICStorage):
    __storage: IStorage
    protocol: str
    host: str
    port: str
    url: str
    app: FastAPI

    def __init__(self, storage: IStorage, adapters: dict = dict({}), autostart=True):
        with open(os.path.join(os.path.dirname(__file__), 'config.json')) as file:
            data = json.load(file)
        self.__storage = storage
        self.protocol = data[CONFIG.PROTOCOL.value]
        self.host = data[CONFIG.HOST.value]
        self.port = data[CONFIG.PORT.value]
        self.url = f'{self.protocol}://{self.host}:{self.port}'
        self.app = FastAPI()
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*'],
        )
        self.app.include_router(Router(storage, self, adapters))

        if autostart:
            self.start()

    def start(self):
        uvicorn.run(self.app, host=self.host, port=self.port)

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
        try:
            return UCGetFundById(self.__storage)(dealId)
        except NotFoundError as err:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))

    def getFundByKold(self, kold: str):
        try:
            return UCGetFundByKold(self.__storage)(kold)
        except NotFoundError as err:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))

    def getDesembById(self, dealId: int):
        try:
            return UCGetDesembById(self.__storage)(dealId)
        except NotFoundError as err:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))

    def getDesembByCcb(self, ccb: str):
        try:
            return UCGetDesembByCcb(self.__storage)(ccb)
        except NotFoundError as err:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))

    def getAmortFundById(self, amortId: int):
        try:
            return UCGetAmortFundById(self.__storage)(amortId)
        except NotFoundError as err:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))

    def getAmortFundsByFundId(self, dealId: int):
        return UCGetAmortFundsByFundId(self.__storage)(dealId)

    def getAmortDesembById(self, amortId: int):
        try:
            return UCGetAmortDesembById(self.__storage)(amortId)
        except NotFoundError as err:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))

    def getAmortDesembsByDesembId(self, dealId: int):
        return UCGetAmortDesembsByDesembId(self.__storage)(dealId)

    def getFundPrincAfterAmortById(self, dealId: int, basedate: date = date.today()):
        try:
            return UCGetFundPrincAfterAmortById(self.__storage)(dealId, basedate)
        except NotFoundError as err:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))

    def getDesembPrincAfterAmortById(self, dealId: int, basedate: date = date.today()):
        try:
            return UCGetDesembPrincAfterAmortById(self.__storage)(dealId, basedate=basedate)
        except NotFoundError as err:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))

    def getAvailableFundsForDesembByCcb(self, ccb: str, basedate: date = date.today()):
        try:
            return UCGetAvailableFundsForDesembByCcb(self.__storage)(ccb, basedate=basedate)
        except NotFoundError as err:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))

    def getAmortsInFundByKold(self, kold: str):
        try:
            return UCGetAmortsInFundByKold(self.__storage)(kold)
        except NotFoundError as err:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))


    def generateFundFlowByKold(self, kold: str):
        try:
            return UCGenerateFundFlowByKold(self.__storage)(kold)
        except NotFoundError as err:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))

    def changeFund(self, desemb: Desemb, newFund: Fund, override=False):
        return UCChangeFund(self.__storage)(desemb, newFund, override)

    def createFund(self, fund, amorts):
        return UCCreateFund(self.__storage)(fund, amorts)

    def createDesemb(self, desemb, amorts):
        return UCCreateDesemb(self.__storage)(desemb, amorts)
