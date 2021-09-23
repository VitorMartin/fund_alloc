from typing import Optional

from pydantic import BaseModel


class BaseResponseModel(BaseModel):
    msg: Optional[str] = ''
