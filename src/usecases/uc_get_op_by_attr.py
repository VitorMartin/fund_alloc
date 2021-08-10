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


class UCGetDesembById:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self, dealId: int) -> Desemb:
        return self.storage.getDesembById(dealId)


class UCGetAmortFundById:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self, amortId: int) -> AmortFund:
        return self.storage.getAmortFundById(amortId)


class UCGetAmortDesembById:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self, amortId: int) -> AmortDesemb:
        return self.storage.getAmortDesembById(amortId)
