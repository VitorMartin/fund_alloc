from datetime import date
from typing import List, Union

from src.interfaces.i_storage import IStorage
from src.models.amort import Amort
from src.models.amort_desemb import AmortDesemb
from src.models.amort_fund import AmortFund
from src.models.desemb import Desemb
from src.models.fund import Fund


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

    def __call__(self, kold: str) -> list[dict[str, Union[Fund, Desemb, AmortFund, AmortDesemb, str, date, float]]]:
        return self.storage.generateFundAvailabilityByKold(kold)
