from src.interfaces.i_storage import IStorage
from src.models.fund import Fund


class UCgetRemainPrincInFundById:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self, dealId: int) -> float:
        return self.storage.getRemainPrincInFundById(dealId)
