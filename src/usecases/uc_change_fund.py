from src.interfaces.i_storage import IStorage
from src.models.desemb import Desemb
from src.models.fund import Fund


class UCChangeFund:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self, desemb: Desemb, newFund: Fund) -> bool:
        return self.storage.changeFund(desemb, newFund)
