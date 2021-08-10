from datetime import date
from typing import Any

from src.models.enums.ccy import CCY
from src.models.enums.dict_keys import *


class Deal:
    dealId: int = None
    ccy: CCY
    princ: float
    ini: date
    venc: date

    def __init__(self, ccy: CCY, princ: float, ini: date, venc: date, pk: int = None):
        self.dealId = pk
        self.ccy = ccy
        self.princ = princ
        self.ini = ini
        self.venc = venc

    def __str__(self):
        return (
            f'{MODEL.DEAL} = {{ '
            f'{DEAL.ID} = {self.dealId},'
            f'\t{DEAL.CCY} = {self.ccy},'
            f'\t{DEAL.PRINC} = {self.princ},'
            f'\t{DEAL.INI} = {self.ini},'
            f'\t{DEAL.VENC} = {self.venc}'
            f'}}'
        )

    def __eq__(self, other: Any):
        return self.__dict__ == other.__dict__

    @staticmethod
    def fromDict(d: dict):
        deal = Deal(
            d[DEAL.CCY.value], d[DEAL.PRINC.value], d[DEAL.INI.value],
            d[DEAL.VENC.value], d[DEAL.ID.value]
        )

        return deal
