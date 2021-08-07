from src.usecases.uc_get_all import *


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
