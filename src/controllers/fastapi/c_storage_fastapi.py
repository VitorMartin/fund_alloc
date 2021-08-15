import json

from controllers.fastapi.enums.status_code import STATUS_CODE
from controllers.fastapi.http import HttpResponse
from models.enums.dict_keys import *
from src.interfaces.i_c_storage import ICStorage
from src.usecases.uc_cash_flows import *
from src.usecases.uc_get_all import *
from src.usecases.uc_get_desembs_in_fund import *
from src.usecases.uc_get_op_by_attr import *
from src.usecases.uc_get_values import *


class CStorageFastAPI(ICStorage):
    __storage: IStorage

    def __init__(self, storage: IStorage):
        self.__storage = storage

    def getAllFunds(self) -> HttpResponse:
        funds = UCGetAllFunds(self.__storage)()
        body = {MODEL.FUND: []}
        for fund in funds:
            body[MODEL.FUND].append(fund.toDict())
        return HttpResponse(body, STATUS_CODE.OK)

    def getAllDesembs(self) -> HttpResponse:
        desembs = UCGetAllDesembs(self.__storage)()
        body = {MODEL.DESEMB: []}
        for desemb in desembs:
            body[MODEL.DESEMB].append(desemb.toDict())
        return HttpResponse(body, STATUS_CODE.OK)

    def getAllAmortFunds(self) -> HttpResponse:
        pass

    def getAllAmortDesembs(self) -> HttpResponse:
        pass

    def getDesembsInFundByKold(self, kold: str) -> HttpResponse:
        pass

    def getFundById(self, dealId: int) -> HttpResponse:
        pass

    def getFundByKold(self, kold: str) -> HttpResponse:
        pass

    def getDesembById(self, dealId: int) -> HttpResponse:
        pass

    def getDesembByCcb(self, ccb: str) -> HttpResponse:
        pass

    def getAmortFundById(self, amortId: int) -> HttpResponse:
        pass

    def getAmortFundsByFundId(self, dealId: int) -> HttpResponse:
        pass

    def getAmortDesembById(self, amortId: int) -> HttpResponse:
        pass

    def getAmortDesembsByDesembId(self, dealId: int) -> HttpResponse:
        pass

    def getFundPrincAfterAmortById(self, dealId: int, basedate: date = date.today()) -> HttpResponse:
        pass

    def getDesembPrincAfterAmortById(self, dealId: int, basedate: date = date.today()) -> HttpResponse:
        pass

    def getAvailableFundsForDesembByCcb(self, ccb: str, basedate: date = date.today()) -> HttpResponse:
        pass

    def generateAmortsInFundByKold(self, kold: str) -> HttpResponse:
        pass

    def generateFundAvailByKold(self, kold: str) -> HttpResponse:
        pass
