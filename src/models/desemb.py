from datetime import date
from typing import Any

from src.controllers.fastapi.http.models import DesembModel
from src.models.deal import Deal
from src.models.enums.ccy import CCY
from src.models.enums.dict_keys import *
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
            f'{MODEL.DESEMB} = {{ '
            f'{DESEMB.ID} = {self.dealId},'
            f'\t{DESEMB.CCB} = {self.ccb},'
            f'\t{DESEMB.CCY} = {self.ccy},'
            f'\t{DESEMB.PRINC} = {self.princ},'
            f'\t{DESEMB.INI} = {self.ini},'
            f'\t{DESEMB.VENC} = {self.venc},'
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

    def toModel(self) -> DesembModel:
        if self.fund is not None:
            return DesembModel(
                dealId=self.dealId,
                ccy=self.ccy,
                princ=self.princ,
                ini=self.ini,
                venc=self.venc,
                fund=self.fund.toModel(),
                ccb=self.ccb
            )
        else:
            return DesembModel(
                dealId=self.dealId,
                ccy=self.ccy,
                princ=self.princ,
                ini=self.ini,
                venc=self.venc,
                fund=None,
                ccb=self.ccb
            )

    def toDict(self):
        return {
            DESEMB.ID: self.dealId,
            DESEMB.CCB: self.ccb,
            DESEMB.CCY: self.ccy,
            DESEMB.PRINC: self.princ,
            DESEMB.INI: self.ini,
            DESEMB.VENC: self.venc,
            MODEL.FUND: {
                FUND.ID: self.fund.dealId,
                FUND.KOLD: self.fund.kold,
                FUND.CCY: self.fund.ccy,
                FUND.PRINC: self.fund.princ,
                FUND.INI: self.fund.ini,
                FUND.VENC: self.fund.venc
            }
        }

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

        return desemb

    @staticmethod
    def fromModel(m: DesembModel):
        if m is None:
            return None
        else:
            return Desemb(
                pk=m.dealId,
                ccy=m.ccy,
                princ=m.princ,
                ini=m.ini,
                venc=m.venc,
                fund=Fund.fromModel(m.fund),
                ccb=m.ccb
            )
