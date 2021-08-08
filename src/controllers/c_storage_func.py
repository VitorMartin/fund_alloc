from src.usecases.uc_get_all import *
from src.usecases.uc_get_desembs_in_fund import *


class CStorageFunc:
    __storage: IStorage

    def __init__(self, storage: IStorage):
        self.storage = storage

    def getAllFunds(self):
        return UCGetAllFunds(self.storage)()

    def getAllDesembs(self):
        return UCGetAllDesembs(self.storage)()

    def getAllAmortFunds(self):
        return UCGetAllAmortFunds(self.storage)()

    def getAllAmortDesembs(self):
        return UCGetAllAmortDesembs(self.storage)()

    def getDesembsInFundByKold(self, kold: str):
        return UCGetDesembsInFundByKold(self.storage)(kold)
