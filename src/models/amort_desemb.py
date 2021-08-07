from datetime import date

from src.models.amort import Amort
from src.models.desemb import Desemb
from src.models.enums.ccy import CCY


class AmortDesemb(Amort):
    desemb: Desemb

    def __init__(self, desemb: Desemb, amortDate: date, ccy: CCY, val: float, pk: int = None):
        super().__init__(amortDate, ccy, val, pk=pk)
        self.desemb = desemb

    def __str__(self):
        return (
            f'amortDesemb = {{ '
            f'pk = {self.pk},'
            f'\tccy = {self.ccy},'
            f'\tval = {self.val},'
            f'\tdate = {self.date},'
            f'\tdesemb = {{ '
            f'pk = {self.desemb.pk},'
            f'ccb = {self.desemb.ccb},'
            f'\tccy = {self.desemb.ccy},'
            f'\tval = {self.desemb.princ}'
            f'\tval = {self.desemb.ini}'
            f'\tdate = {self.desemb.venc},'
            f'\tfund = {{ '
            f'pk = {self.desemb.fund.pk},'
            f'\tkold = {self.desemb.fund.kold},'
            f'\tccy = {self.desemb.fund.ccy},'
            f'\tprinc = {self.desemb.fund.princ},'
            f'\tini = {self.desemb.fund.ini},'
            f'\tvenc = {self.desemb.fund.venc} '
            f'}} '
            f'}} '
            f'}}'
        )
