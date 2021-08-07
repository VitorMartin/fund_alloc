from datetime import date

from src.models.deal import Deal
from src.models.enums.ccy import CCY


class Fund(Deal):
    kold: str

    def __init__(self, kold: str, ccy: CCY, princ: float, ini: date, venc: date, pk: int = None):
        super().__init__(ccy, princ, ini, venc, pk=pk)
        self.kold = kold

    def __str__(self):
        return (
            f'fund = {{ '
            f'pk = {self.pk},'
            f'\tkold = {self.kold},'
            f'\tccy = {self.ccy},'
            f'\tprinc = {self.princ},'
            f'\tini = {self.ini},'
            f'\tvenc = {self.venc}'
            f'}}'
        )
