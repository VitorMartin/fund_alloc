from datetime import date

from src.models.amort import Amort
from src.models.enums.ccy import CCY
from src.models.enums.dict_keys import *
from src.models.fund import Fund


class AmortFund(Amort):
    fund: Fund

    def __init__(self, fund: Fund, amortData: date, ccy: CCY, val: float, pk: int = None):
        super().__init__(amortData, ccy, val, pk=pk)
        self.fund = fund

    def __str__(self):
        return (
            f'{MODEL.AMORT_FUND} = {{ '
            f'{AMORT_FUND.ID} = {self.amortId},'
            f'\t{AMORT_FUND.CCY} = {self.ccy},'
            f'\t{AMORT_FUND.VAL} = {self.val},'
            f'\t{AMORT_FUND.DATA} = {self.data},'
            f'\t{MODEL.FUND} = {{ '
            f'{FUND.ID} = {self.fund.dealId},'
            f'\t{FUND.KOLD} = {self.fund.kold},'
            f'\t{FUND.CCY} = {self.fund.ccy},'
            f'\t{FUND.PRINC} = {self.fund.princ},'
            f'\t{FUND.INI} = {self.fund.ini},'
            f'\t{FUND.VENC} = {self.fund.venc} '
            f'}} '
            f'}}'
        )
