from datetime import date

from src.models.deal import Deal
from src.models.enums.ccy import CCY
from src.models.fund import Fund


class Desemb(Deal):
    fund: Fund
    ccb: str

    def __init__(
            self, fund: Fund, ccb: str, ccy: CCY, princ: float, ini: date, venc: date, pk: int = None
    ):
        super().__init__(ccy, princ, ini, venc, pk=pk)
        self.fund = fund
        self.ccb = ccb

    def __str__(self):
        return (
            f'desemb = {{ '
            f'pk = {self.pk},'
            f'\tccb = {self.ccb},'
            f'\tccy = {self.ccy},'
            f'\tprinc = {self.princ},'
            f'\tini = {self.ini},'
            f'\tvenc = {self.venc},'
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

    @staticmethod
    def fromDict(d: dict):
        fund = Fund(d['fund_kold'], d['fund_ccy'], d['fund_princ'], d['fund_ini'].date(), d['fund_venc'].date(), d['fund_id'])
        desemb = Desemb(
            fund, d['desemb_ccb'], d['desemb_ccy'], d['desemb_princ'],
            d['desemb_ini'].date(), d['desemb_venc'].date(), d['desemb_id']
        )

        return desemb
