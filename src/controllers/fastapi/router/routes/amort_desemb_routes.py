from fastapi import APIRouter

from src.controllers.fastapi.errors.errors import *
from src.controllers.fastapi.http.responses import *
from src.interfaces.i_c_storage import ICStorage
from src.models.amort_desemb import AmortDesemb


class AmortDesembRoutes(APIRouter):
    def __init__(self, ctrl: ICStorage):
        super(AmortDesembRoutes, self).__init__(
            prefix='/amort_desemb'
        )

        @self.get('/', response_model=Union[AmortDesembsModel, AmortDesembModel])
        async def getAllAmortDesembs(amortId: int = None, dealId: int = None):
            if amortId is None and dealId is None:
                return AmortDesembsModel(
                    amortDesembs=[AmortDesemb.toModel(amortDesemb) for amortDesemb in ctrl.getAllAmortDesembs()]
                )
            elif amortId is not None and dealId is None:
                return AmortDesemb.toModel(ctrl.getAmortDesembById(amortId))
            elif dealId is not None and amortId is None:
                return AmortDesembsModel(
                    amortDesembs=[
                        AmortDesemb.toModel(amortDesemb) for amortDesemb in ctrl.getAmortDesembsByDesembId(dealId)
                    ]
                )
            else:
                raise TooManyArgsException()
