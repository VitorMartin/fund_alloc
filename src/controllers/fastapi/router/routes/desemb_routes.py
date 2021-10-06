from fastapi import APIRouter

from src.controllers.fastapi.errors.errors import *
from src.controllers.fastapi.http.responses import *
from src.interfaces.i_c_storage import ICStorage
from src.models.desemb import Desemb


class DesembRoutes(APIRouter):
    def __init__(self, ctrl: ICStorage):
        super(DesembRoutes, self).__init__(
            prefix='/desemb'
        )

        @self.get('/', response_model=Union[DesembsModel, DesembModel])
        async def getAllDesembs(dealId: int = None, ccb: str = None, kold: str = None):
            if dealId is None and ccb is None and kold is None:
                return DesembsModel(desembs=[Desemb.toModel(desemb) for desemb in ctrl.getAllDesembs()])
            elif dealId is not None and ccb is None and kold is None:
                return Desemb.toModel(ctrl.getDesembById(dealId))
            elif ccb is not None and dealId is None and kold is None:
                return Desemb.toModel(ctrl.getDesembByCcb(ccb))
            elif kold is not None and dealId is None and ccb is None:
                return DesembsModel(desembs=[Desemb.toModel(desemb) for desemb in ctrl.getDesembsInFundByKold(kold)])
            else:
                raise TooManyArgsException()

        @self.get('/princ', response_model=PrincModel)
        async def getDesembPrincAfterAmort(dealId: int, basedate: date = None):
            if basedate is None:
                return PrincModel(princ=ctrl.getDesembPrincAfterAmortById(dealId))
            else:
                return PrincModel(princ=ctrl.getDesembPrincAfterAmortById(dealId, basedate))
