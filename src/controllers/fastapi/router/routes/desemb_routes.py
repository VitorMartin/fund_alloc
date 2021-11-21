from fastapi import APIRouter

from src.controllers.fastapi.errors.errors import *
from src.controllers.fastapi.http.responses import *
from src.interfaces.i_c_storage import ICStorage
from src.models.amort_desemb import AmortDesemb
from src.models.desemb import Desemb
from src.models.fund import Fund


class DesembRoutes(APIRouter):
    def __init__(self, ctrl: ICStorage):
        super().__init__(
            prefix='/desemb'
        )

        @self.post('/', response_model=DesembModel)
        async def createFund(desemb: DesembModel, amorts: AmortDesembsModel):
            desemb = Desemb.fromModel(desemb)
            amortsTmp = []
            for amortModel in amorts.amortDesembs:
                amortsTmp.append(AmortDesemb.fromModel(amortModel))
            amorts = amortsTmp.copy()

            return Desemb.toModel(ctrl.createDesemb(desemb, amorts))

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

        @self.get('/availability', response_model=FundsModel)
        async def getAvailableFundsForDesembByCcb(ccb: str = None, basedate: date = None):
            if ccb is None:
                raise MissingArgsException()
            else:
                if basedate is None:
                    return FundsModel(
                        funds=[Fund.toModel(fund) for fund in ctrl.getAvailableFundsForDesembByCcb(ccb)]
                    )
                else:
                    return FundsModel(
                        funds=[Fund.toModel(fund) for fund in ctrl.getAvailableFundsForDesembByCcb(ccb, basedate)]
                    )
