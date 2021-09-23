from typing import List

from pydantic import BaseModel


class RootModel(BaseModel):
    repository_type: str
    controller_type: str
    adapters: List[str]


class ValueModel(BaseModel):
    value: float
