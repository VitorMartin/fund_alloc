from typing import List

from src.interfaces.i_storage import IStorage
from src.models.desemb import Desemb


class UCGetDesembsInFundByKold:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self, kold: str) -> List[Desemb]:
        return self.storage.getDesembsInFundByKold(kold)
