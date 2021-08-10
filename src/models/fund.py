from datetime import date
from typing import Any

from src.models.deal import Deal
from src.models.enums.ccy import CCY
from src.models.enums.dict_keys import *


class Fund(Deal):
    kold: str

    def __init__(self, kold: str, ccy: CCY, princ: float, ini: date, venc: date, pk: int = None):
        super().__init__(ccy, princ, ini, venc, pk=pk)
        self.kold = kold

    def __str__(self):
        return (
            f'{MODEL.FUND} = {{ '
            f'{FUND.ID} = {self.dealId},'
            f'\t{FUND.KOLD} = {self.kold},'
            f'\t{FUND.CCY} = {self.ccy},'
            f'\t{FUND.PRINC} = {self.princ},'
            f'\t{FUND.INI} = {self.ini},'
            f'\t{FUND.VENC} = {self.venc}'
            f'}}'
        )

    def __eq__(self, other: Any):
        return self.__dict__ == other.__dict__

    @staticmethod
    def fromDict(d: dict):
        fund = Fund(
            d[FUND.KOLD.value], d[FUND.CCY.value], d[FUND.PRINC.value], d[FUND.INI.value],
            d[FUND.VENC.value], d[FUND.ID.value]
        )

        return fund
