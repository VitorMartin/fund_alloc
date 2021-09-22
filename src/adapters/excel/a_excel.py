from datetime import date

from src.controllers.fastapi.http import *
from src.interfaces.i_c_storage import ICStorage
from src.models.enums.dict_keys import *


class AExcel:
    """
    Flattens all HTTP responses' dicts from CStorageFastAPI.
    """
    ctrl: ICStorage

    def __init__(self, _ctrl: ICStorage):
        self.ctrl = _ctrl

    def getAllFunds(self) -> HttpResponse:
        newDict = {}
        httpRes = self.ctrl.getAllFunds()
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
        httpRes = self.ctrl.getAllDesembs()
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
        return self.ctrl.getAllAmortFunds()

    def getAllAmortDesembs(self) -> HttpResponse:
        return self.ctrl.getAllAmortDesembs()

    def getDesembsInFundByKold(self, kold: str) -> HttpResponse:
        return self.ctrl.getDesembsInFundByKold(kold)

    def getFundById(self, dealId: int) -> HttpResponse:
        return self.ctrl.getFundById(dealId)

    def getFundByKold(self, kold: str) -> HttpResponse:
        return self.ctrl.getFundByKold(kold)

    def getDesembById(self, dealId: int) -> HttpResponse:
        return self.ctrl.getDesembById(dealId)

    def getDesembByCcb(self, ccb: str) -> HttpResponse:
        return self.ctrl.getDesembByCcb(ccb)

    def getAmortFundById(self, amortId: int) -> HttpResponse:
        return self.ctrl.getAmortFundById(amortId)

    def getAmortFundsByFundId(self, dealId: int) -> HttpResponse:
        return self.ctrl.getAmortFundsByFundId(dealId)

    def getAmortDesembById(self, amortId: int) -> HttpResponse:
        return self.ctrl.getAmortDesembById(amortId)

    def getAmortDesembsByDesembId(self, dealId: int) -> HttpResponse:
        return self.ctrl.getAmortDesembsByDesembId(dealId)

    def getFundPrincAfterAmortById(self, dealId: int, basedate: date = date.today()) -> HttpResponse:
        return self.ctrl.getFundPrincAfterAmortById(dealId, basedate)

    def getDesembPrincAfterAmortById(self, dealId: int, basedate: date = date.today()) -> HttpResponse:
        return self.ctrl.getDesembPrincAfterAmortById(dealId, basedate)

    def getAvailableFundsForDesembByCcb(self, ccb: str, basedate: date = date.today()) -> HttpResponse:
        return self.ctrl.getAvailableFundsForDesembByCcb(ccb, basedate)

    def generateAmortsInFundByKold(self, kold: str) -> HttpResponse:
        return self.ctrl.generateAmortsInFundByKold(kold)

    def generateFundAvailByKold(self, kold: str) -> HttpResponse:
        return self.ctrl.generateFundAvailByKold(kold)
