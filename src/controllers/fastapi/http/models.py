from datetime import date

from pydantic import BaseModel

from src.models.enums.ccy import CCY


class DealModel(BaseModel):
    dealId: int = None
    ccy: CCY
    princ: float
    ini: date
    venc: date


class FundModel(BaseModel):
    dealId: int = None
    ccy: CCY
    princ: float
    ini: date
    venc: date

    kold: str


class DesembModel(BaseModel):
    dealId: int = None
    ccy: CCY
    princ: float
    ini: date
    venc: date

    fund: FundModel

    ccb: str


class AmortModel(BaseModel):
    amortId: int = None
    data: date
    ccy: CCY
    val: float


class AmortFundModel(BaseModel):
    amortId: int = None
    data: date
    ccy: CCY
    val: float

    fund: FundModel


class AmortDesembModel(BaseModel):
    amortId: int = None
    data: date
    ccy: CCY
    val: float

    desemb: DesembModel
