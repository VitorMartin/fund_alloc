from typing import List

from src.models.amort_desemb import AmortDesemb
from src.models.amort_fund import AmortFund
from src.models.desemb import Desemb
from src.models.fund import Fund
from src.usecases.uc_get_all import *
from src.usecases.uc_get_desembs_in_fund import *


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
