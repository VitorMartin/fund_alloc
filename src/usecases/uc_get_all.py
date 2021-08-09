from typing import List

from src.interfaces.i_storage import IStorage
from src.models.amort_desemb import AmortDesemb
from src.models.amort_fund import AmortFund
from src.models.desemb import Desemb
from src.models.fund import Fund


class UCGetAllFunds:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self) -> List[Fund]:
        return self.storage.getAllFunds()


class UCGetAllDesembs:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self) -> List[Desemb]:
        return self.storage.getAllDesembs()


class UCGetAllAmortFunds:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self) -> List[AmortFund]:
        return self.storage.getAllAmortFunds()


class UCGetAllAmortDesembs:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self) -> List[AmortDesemb]:
        return self.storage.getAllAmortDesembs()
