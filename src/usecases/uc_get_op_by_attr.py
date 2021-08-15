from typing import List

from src.interfaces.i_storage import IStorage
from src.models.amort_desemb import AmortDesemb
from src.models.amort_fund import AmortFund
from src.models.desemb import Desemb
from src.models.fund import Fund


class UCGetFundById:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self, dealId: int) -> Fund:
        return self.storage.getFundById(dealId)


class UCGetFundByKold:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self, kold: str) -> Fund:
        return self.storage.getFundByKold(kold)


class UCGetDesembById:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self, dealId: int) -> Desemb:
        return self.storage.getDesembById(dealId)

    
class UCGetDesembByCcb:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self, ccb: str) -> Desemb:
        return self.storage.getDesembByCcb(ccb)


class UCGetAmortFundById:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self, amortId: int) -> AmortFund:
        return self.storage.getAmortFundById(amortId)


class UCGetAmortFundsByFundId:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self, dealId: int) -> List[AmortFund]:
        return self.storage.getAmortFundsByFundId(dealId)


class UCGetAmortDesembById:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self, amortId: int) -> AmortDesemb:
        return self.storage.getAmortDesembById(amortId)


class UCGetAmortDesembsByDesembId:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self, dealId: int) -> List[AmortDesemb]:
        return self.storage.getAmortDesembsByDesembId(dealId)
