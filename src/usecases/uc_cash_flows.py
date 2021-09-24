from datetime import date
from typing import Any, List

from src.interfaces.i_storage import IStorage
from src.models.amort import Amort


class UCGenerateFundFlowByKold:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self, kold: str) -> List[Amort]:
        return self.storage.generateFundFlowByKold(kold)


class UCGenerateFundAvailabilityByKold:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self, kold: str) -> List[dict[Any, str, date, float, float, float, float, float]]:
        return self.storage.generateFundAvailByKold(kold)
