from datetime import date

from src.models.enums.ccy import CCY


class Deal:
    pk: int = None
    ccy: CCY
    princ: float
    ini: date
    venc: date

    def __init__(self, ccy: CCY, princ: float, ini: date, venc: date, pk: int = None):
        self.pk = pk
        self.ccy = ccy
        self.princ = princ
        self.ini = ini
        self.venc = venc

    def __str__(self):
        return (
            f'deal = {{ '
            f'pk = {self.pk},'
            f'\tccy = {self.ccy},'
            f'\tprinc = {self.princ},'
            f'\tini = {self.ini},'
            f'\tvenc = {self.venc}'
            f'}}'
        )
