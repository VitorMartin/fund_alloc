from typing import Union

from src.interfaces.i_storage import IStorage
from src.models.desemb import Desemb
from src.models.fund import Fund
from src.repositories.errors.repository_error import RepositoryError
from src.usecases.errors.ccy_break_error import CcyBreakError
from src.usecases.errors.date_break_error import DateBreakError
from src.usecases.errors.value_break_error import ValueBreakError


class UCChangeFund:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self, desemb: Desemb, newFund: Union[Fund, None], override) -> Desemb:
        if override:
            return self.storage.changeFund(desemb, newFund)
        else:
            if newFund is None:
                try:
                    return self.storage.changeFund(desemb, newFund)
                except RepositoryError as err:
                    raise err
            if desemb.ccy != newFund.ccy:
                raise CcyBreakError()
            elif self.storage.getFundPrincAfterAmortById(newFund.dealId) - desemb.princ < 0:
                raise ValueBreakError()
            elif desemb.venc > newFund.venc:
                raise DateBreakError()
            else:
                try:
                    return self.storage.changeFund(desemb, newFund)
                except RepositoryError as err:
                    raise err
