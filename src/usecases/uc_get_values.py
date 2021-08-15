from datetime import date

from src.interfaces.i_storage import IStorage


class UCgetRemainPrincInFundById:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self, dealId: int, basedate: date = date.today()) -> float:
        return self.storage.getFundPrincAfterAmortById(dealId, basedate=basedate)


class UCgetRemainPrincInDesembById:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self, dealId: int, basedate: date = date.today()) -> float:
        return self.storage.getDesembPrincAfterAmortById(dealId, basedate=basedate)
