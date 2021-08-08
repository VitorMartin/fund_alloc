from datetime import date

from src.models.enums.ccy import CCY
from src.models.enums.dict_keys import *


class Amort:
    amortId: int = None
    data: date
    ccy: CCY
    val: float

    def __init__(self, amortData: date, ccy: CCY, val: float, pk: int = None):
        self.amortId = pk
        self.data = amortData
        self.ccy = ccy
        self.val = val

    def __str__(self):
        return (
            f'{MODEL.AMORT} = {{ '
            f'{AMORT.ID} = {self.amortId},'
            f'\t{AMORT.CCY} = {self.ccy},'
            f'\t{AMORT.VAL} = {self.val},'
            f'\t{AMORT.DATA} = {self.data}'
            f'}}'
        )
