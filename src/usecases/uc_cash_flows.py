from typing import List

from src.interfaces.i_storage import IStorage
from src.models.amort import Amort


class UCGenerateFundCashFlowByKold:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self, kold: str) -> List[Amort]:
        return self.storage.generateAmortsInFundByKold(kold)
