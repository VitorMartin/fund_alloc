from typing import List, Union

from src.controllers.fastapi.http.models import *


class RootModel(BaseModel):
    repository_type: str
    controller_type: str
    adapters: List[str]


class FundsModel(BaseModel):
    funds: List[FundModel]


class DesembsModel(BaseModel):
    desembs: List[DesembModel]


class AmortFundsModel(BaseModel):
    amortFunds: List[AmortFundModel]


class AmortDesembsModel(BaseModel):
    amortDesembs: List[AmortDesembModel]


class PrincModel(BaseModel):
    princ: float


class CashFlowModel(BaseModel):
    amorts: List[Union[AmortFundModel, AmortDesembModel]]


class FundAvailabilityMovementModel(BaseModel):
    op: Union[FundModel, DesembModel, AmortFundModel, AmortDesembModel]
    type: str
    data: date
    val: float
    fundPrinc: float
    desembPrinc: float
    availBefore: float
    availAfter: float


class FundAvailabilityModel(BaseModel):
    availability: List[FundAvailabilityMovementModel]
