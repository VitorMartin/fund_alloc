from datetime import date
from typing import Any

from src.controllers.fastapi.http.models import AmortDesembModel
from src.models.amort import Amort
from src.models.desemb import Desemb
from src.models.enums.ccy import CCY
from src.models.enums.dict_keys import *
from src.models.fund import Fund


class AmortDesemb(Amort):
    desemb: Desemb

    def __init__(self, desemb: Desemb, amortData: date, ccy: CCY, val: float, pk: int = None):
        super().__init__(amortData, ccy, val, pk=pk)
        self.desemb = desemb

    def __str__(self):
        return (
            f'{MODEL.AMORT_DESEMB} = {{ '
            f'{AMORT_DESEMB.ID} = {self.amortId},'
            f'\t{AMORT_DESEMB.CCY} = {self.ccy},'
            f'\t{AMORT_DESEMB.VAL} = {self.val},'
            f'\t{AMORT_DESEMB.DATA} = {self.data},'
            f'\t{MODEL.DESEMB} = {{ '
            f'{DESEMB.ID} = {self.desemb.dealId},'
            f'{DESEMB.CCB} = {self.desemb.ccb},'
            f'\t{DESEMB.CCY} = {self.desemb.ccy},'
            f'\t{DESEMB.PRINC} = {self.desemb.princ}'
            f'\t{DESEMB.INI} = {self.desemb.ini}'
            f'\t{DESEMB.VENC} = {self.desemb.venc},'
            f'\t{MODEL.FUND} = {{ '
            f'{FUND.ID} = {self.desemb.fund.dealId},'
            f'\t{FUND.KOLD} = {self.desemb.fund.kold},'
            f'\t{FUND.CCY} = {self.desemb.fund.ccy},'
            f'\t{FUND.PRINC} = {self.desemb.fund.princ},'
            f'\t{FUND.INI} = {self.desemb.fund.ini},'
            f'\t{FUND.VENC} = {self.desemb.fund.venc} '
            f'}} '
            f'}} '
            f'}}'
        )

    def __eq__(self, other: Any):
        return self.__dict__ == other.__dict__

    def toModel(self) -> AmortDesembModel:
        return AmortDesembModel(
            amortId=self.amortId,
            data=self.data,
            ccy=self.ccy,
            val=self.val,
            desemb=self.desemb.toModel()
        )

    @staticmethod
    def fromDict(d: dict):
        fund = Fund(
            d[FUND.KOLD.value], d[FUND.CCY.value], d[FUND.PRINC.value], d[FUND.INI.value],
            d[FUND.VENC.value], d[FUND.ID.value]
        )
        desemb = Desemb(
            fund, d[DESEMB.CCB.value], d[DESEMB.CCY.value], d[DESEMB.PRINC.value],
            d[DESEMB.INI.value], d[DESEMB.VENC.value], d[DESEMB.ID.value]
        )
        amortDesemb = AmortDesemb(
            desemb, d[AMORT_DESEMB.DATA.value], d[AMORT_DESEMB.CCY.value],
            d[AMORT_DESEMB.VAL.value], d[AMORT_DESEMB.ID.value]
        )

        return amortDesemb

    @staticmethod
    def fromModel(m: AmortDesembModel):
        return AmortDesemb(
            pk=m.amortId,
            amortData=m.data,
            ccy=m.ccy,
            val=m.val,
            desemb=Desemb.fromModel(m.desemb)
        )
