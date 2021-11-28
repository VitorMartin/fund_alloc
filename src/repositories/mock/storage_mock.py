from typing import List

from src.interfaces.i_storage import IStorage
from src.models.amort_desemb import AmortDesemb
from src.models.amort_fund import AmortFund
from src.models.desemb import Desemb
from src.models.fund import Fund
from src.repositories.errors.creating_errors import *
from src.repositories.errors.getter_errors import *
from src.repositories.errors.repository_error import *
from src.repositories.mock.mock_data import MockData


class StorageMock(IStorage):
    __funds: list[Fund]
    __desembs: list[Desemb]
    __amortFunds: list[AmortFund]
    __amortDesembs: list[AmortDesemb]

    def __init__(
            self, funds: list[Fund] = MockData.funds, desembs: list[Desemb] = MockData.desembs,
            amortFunds: list[AmortFund] = MockData.amortFunds, amortDesembs: list[AmortDesemb] = MockData.amortDesembs
    ):
        self.__funds = funds
        self.__desembs = desembs
        self.__amortFunds = amortFunds
        self.__amortDesembs = amortDesembs

    def getAllFunds(self) -> List[Fund]:
        return self.__funds

    def getAllDesembs(self) -> List[Desemb]:
        return self.__desembs

    def getAllAmortFunds(self) -> List[AmortFund]:
        return self.__amortFunds

    def getAllAmortDesembs(self) -> List[AmortDesemb]:
        return self.__amortDesembs

    def getDesembsInFundByKold(self, kold: str) -> List[Desemb]:
        desembs = []
        for desemb in self.__desembs:
            if desemb.fund is not None:
                if desemb.fund.kold == kold:
                    desembs.append(desemb)
        return desembs

    def getFundById(self, dealId: int) -> Fund:
        fundsFound = [fund for fund in self.__funds if fund.dealId == dealId]
        if len(fundsFound) == 0:
            raise NotFoundError
        return fundsFound[0]

    def getFundByKold(self, kold: str) -> Fund:
        fundsFound = [fund for fund in self.__funds if fund.kold == kold]
        if len(fundsFound) == 0:
            raise NotFoundError
        else:
            return fundsFound[0]

    def getDesembById(self, dealId: int) -> Desemb:
        desembsFound = [desemb for desemb in self.__desembs if desemb.dealId == dealId]
        if len(desembsFound) == 0:
            raise NotFoundError
        else:
            return desembsFound[0]

    def getDesembByCcb(self, ccb: str) -> Desemb:
        desembsFound = [desemb for desemb in self.__desembs if desemb.ccb == ccb]
        if len(desembsFound) == 0:
            raise NotFoundError
        else:
            return desembsFound[0]

    def getAmortFundById(self, amortId: int) -> AmortFund:
        amortFundsFound = [amortFund for amortFund in self.__amortFunds if amortFund.amortId == amortId]
        if len(amortFundsFound) == 0:
            raise NotFoundError
        else:
            return amortFundsFound[0]

    def getAmortFundsByFundId(self, dealId: int) -> List[AmortFund]:
        return [amortFund for amortFund in self.__amortFunds if amortFund.fund.dealId == dealId]

    def getAmortDesembById(self, amortId: int) -> AmortDesemb:
        amortDesembsFound = [amortDesemb for amortDesemb in self.__amortDesembs if amortDesemb.amortId == amortId]
        if len(amortDesembsFound) == 0:
            raise NotFoundError
        else:
            return amortDesembsFound[0]

    def getAmortDesembsByDesembId(self, dealId: int) -> List[AmortDesemb]:
        return [amortDesemb for amortDesemb in self.__amortDesembs if amortDesemb.desemb.dealId == dealId]

    # def getFundPrincAfterAmortById(self, dealId: int, basedate: date = date.today()) -> float:
    #     pass

    # def getDesembPrincAfterAmortById(self, dealId: int, basedate: date = date.today()) -> float:
    #     pass

    # def getAvailableFundsForDesembByCcb(self, ccb: str, basedate: date = date.today()) -> List[Fund]:
    #     pass

    # def getAmortsInFundByKold(self, kold: str) -> List[Amort]:
    #     pass

    # def generateFundFlowByKold(self, kold: str) \
    #         -> List[dict[Any, str, date, float, float, float, float, float]]:
    #     pass

    def changeFund(self, desemb, newFund):
        try:
            index = self.__desembs.index(desemb)
            desemb.fund = newFund
            self.__desembs[index] = desemb
            return desemb
        except ValueError:
            raise DealNotFoundError
        except IndexError:
            raise RepositoryError

    def createFund(self, fund, amorts):
        dealIdFound = False
        dealId = 1
        while not dealIdFound:
            try:
                self.getFundById(dealId)
            except NotFoundError:
                fund.dealId = dealId
                dealIdFound = True
            else:
                dealId += 1

        amortIdOffset = 0
        for amort in amorts:
            amortIdFound = False
            amortId = 1
            while not amortIdFound:
                try:
                    self.getAmortFundById(amortId)
                except NotFoundError:
                    amort.amortId = amortId + amortIdOffset
                    amort.fund.dealId = dealId
                    amortIdOffset += 1
                    amortIdFound = True
                else:
                    amortId += 1

        try:
            self.__funds.append(fund)
            [self.__amortFunds.append(amort) for amort in amorts]
            return fund
        except:
            raise UnableToCreateDealError

    def createDesemb(self, desemb, amorts):
        dealIdFound = False
        dealId = 1
        while not dealIdFound:
            try:
                self.getDesembById(dealId)
            except NotFoundError:
                desemb.dealId = dealId
                dealIdFound = True
            else:
                dealId += 1

        amortIdOffset = 0
        for amort in amorts:
            amortIdFound = False
            amortId = 1
            while not amortIdFound:
                try:
                    self.getAmortDesembById(amortId)
                except NotFoundError:
                    amort.amortId = amortId + amortIdOffset
                    amort.desemb.dealId = dealId
                    amortIdOffset += 1
                    amortIdFound = True
                else:
                    amortId += 1

        try:
            self.__desembs.append(desemb)
            [self.__amortDesembs.append(amort) for amort in amorts]
            return desemb
        except:
            raise UnableToCreateDealError
