from typing import List

from src.interfaces.i_storage import IStorage
from src.models.amort_desemb import AmortDesemb
from src.models.amort_fund import AmortFund
from src.models.desemb import Desemb
from src.models.fund import Fund
from src.repositories.errors.repository_error import *
from src.usecases.errors.invalid_deal_error import *
from src.usecases.errors.missing_amort_error import MissingAmortError
from src.usecases.errors.repeated_deal_error import *


class UCCreateFund:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self, fund: Fund, amorts: List[AmortFund]):
        if len(amorts) == 0:
            raise MissingAmortError
        else:
            try:
                self.storage.getFundByKold(fund.kold)
            except NotFoundError:
                return self.storage.createFund(fund, amorts)
            else:
                raise RepeatedDealError


class UCCreateDesemb:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self, desemb: Desemb, amorts: List[AmortDesemb]):
        if len(amorts) == 0:
            raise MissingAmortError
        else:
            try:
                self.storage.getDesembByCcb(desemb.ccb)
            except NotFoundError:
                if desemb.fund is not None:
                    try:
                        self.storage.getFundByKold(desemb.fund.kold)
                    except NotFoundError:
                        raise InvalidDealError
                    else:
                        return self.storage.createDesemb(desemb, amorts)
                else:
                    return self.storage.createDesemb(desemb, amorts)
            else:
                raise RepeatedDealError
