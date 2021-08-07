from datetime import date

from src.models.enums.ccy import CCY


class Amort:
    pk: int = None
    date: date
    ccy: CCY
    val: float

    def __init__(self, amortDate: date, ccy: CCY, val: float, pk: int = None):
        self.pk = pk
        self.date = amortDate
        self.ccy = ccy
        self.val = val

    def __str__(self):
        return (
            f'amort = {{ '
            f'pk = {self.pk},'
            f'\tccy = {self.ccy},'
            f'\tval = {self.val},'
            f'\tdate = {self.date}'
            f'}}'
        )
