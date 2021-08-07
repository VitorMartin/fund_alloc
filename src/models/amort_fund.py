from datetime import date

from src.models.amort import Amort
from src.models.enums.ccy import CCY
from src.models.fund import Fund


class AmortFund(Amort):
    fund: Fund

    def __init__(self, fund: Fund, amortDate: date, ccy: CCY, val: float, pk: int = None):
        super().__init__(amortDate, ccy, val, pk=pk)
        self.fund = fund

    def __str__(self):
        return (
            f'amortFund = {{ '
            f'pk = {self.pk},'
            f'\tccy = {self.ccy},'
            f'\tval = {self.val},'
            f'\tdate = {self.date},'
            f'\tfund = {{ '
            f'pk = {self.fund.pk},'
            f'\tkold = {self.fund.kold},'
            f'\tccy = {self.fund.ccy},'
            f'\tprinc = {self.fund.princ},'
            f'\tini = {self.fund.ini},'
            f'\tvenc = {self.fund.venc} '
            f'}} '
            f'}}'
        )
