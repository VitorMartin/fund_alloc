from datetime import date
from typing import Any

from controllers.fastapi.http.models import AmortFundModel
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

    def __eq__(self, other: Any):
        return self.__dict__ == other.__dict__

    def toModel(self) -> AmortFundModel:
        return AmortFundModel(
            amortId=self.amortId,
            data=self.data,
            ccy=self.ccy,
            val=self.val,
            fund=self.fund.toModel()
        )

    @staticmethod
    def fromDict(d: dict):
        fund = Fund(
            d[FUND.KOLD.value], d[FUND.CCY.value], d[FUND.PRINC.value], d[FUND.INI.value],
            d[FUND.VENC.value], d[FUND.ID.value]
        )
        amortFund = AmortFund(
            fund, d[AMORT_FUND.DATA.value], d[AMORT_FUND.CCY.value], d[AMORT_FUND.VAL.value], d[AMORT_FUND.ID.value]
        )

        return amortFund
