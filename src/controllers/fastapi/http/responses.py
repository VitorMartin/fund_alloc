from typing import List

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


class ValueModel(BaseModel):
    value: float
