from fastapi import APIRouter

from src.controllers.fastapi.errors.errors import *
from src.controllers.fastapi.http.responses import *
from src.interfaces.i_c_storage import ICStorage
from src.models.amort_desemb import AmortDesemb
from src.models.amort_fund import AmortFund
from src.models.desemb import Desemb
from src.models.enums.dict_keys import MOVEMENT
from src.models.fund import Fund


class FundRoutes(APIRouter):
    def __init__(self, ctrl: ICStorage):
        super(FundRoutes, self).__init__(
            prefix='/fund'
        )

        @self.get('/', response_model=Union[FundsModel, FundModel])
        async def getAllFunds(dealId: int = None, kold: str = None):
            if dealId is None and kold is None:
                return FundsModel(funds=[Fund.toModel(fund) for fund in ctrl.getAllFunds()])
            elif dealId is not None and kold is None:
                return Fund.toModel(ctrl.getFundById(dealId))
            elif kold is not None and dealId is None:
                return Fund.toModel(ctrl.getFundByKold(kold))
            else:
                raise TooManyArgsException()

        @self.get('/princ', response_model=PrincModel)
        async def getFundPrincAfterAmort(dealId: int, basedate: date = None):
            if basedate is None:
                return PrincModel(princ=ctrl.getFundPrincAfterAmortById(dealId))
            else:
                return PrincModel(princ=ctrl.getFundPrincAfterAmortById(dealId, basedate))

        @self.get('/availability', response_model=Union[FundsModel, FundAvailabilityModel])
        async def getAvailableFundsForDesembByCcb(ccb: str = None, basedate: date = None, kold: str = None):
            if kold is None:
                if ccb is None:
                    raise MissingArgsException()
                else:
                    if basedate is None:
                        return FundsModel(
                            funds=[Fund.toModel(fund) for fund in ctrl.getAvailableFundsForDesembByCcb(ccb)])
                    else:
                        return FundsModel(
                            funds=[Fund.toModel(fund) for fund in ctrl.getAvailableFundsForDesembByCcb(ccb, basedate)]
                        )
            else:
                if ccb is None and basedate is None:
                    availabilityModel = []
                    availability = ctrl.generateFundAvailabilityByKold(kold)
                    for avail in availability:
                        if isinstance(avail[MOVEMENT.OP.value], Fund):
                            opModel = Fund.toModel(avail[MOVEMENT.OP.value])
                        elif isinstance(avail[MOVEMENT.OP.value], Desemb):
                            opModel = Desemb.toModel(avail[MOVEMENT.OP.value])
                        elif isinstance(avail[MOVEMENT.OP.value], AmortFund):
                            opModel = AmortFund.toModel(avail[MOVEMENT.OP.value])
                        elif isinstance(avail[MOVEMENT.OP.value], AmortDesemb):
                            opModel = AmortDesemb.toModel(avail[MOVEMENT.OP.value])
                        else:
                            raise InternalServerError()

                        availabilityModel.append(FundAvailabilityMovementModel(
                            op=opModel,
                            type=avail[MOVEMENT.TYPE.value],
                            data=avail[MOVEMENT.DATA.value],
                            val=avail[MOVEMENT.VAL.value],
                            fundPrinc=avail[MOVEMENT.FUND_PRINC.value],
                            desembPrinc=avail[MOVEMENT.DESEMB_PRINC.value],
                            availBefore=avail[MOVEMENT.AVAIL_BEFORE.value],
                            availAfter=avail[MOVEMENT.AVAIL_AFTER.value]
                        ))
                    return FundAvailabilityModel(availability=availabilityModel)
                else:
                    raise TooManyArgsException()

        @self.get('/flow')
        async def generateFundFlowByKold(kold: str = None):
            if kold is None:
                raise MissingArgsException()
            else:
                flowModel = []
                flow = ctrl.generateFundFlowByKold(kold)
                for movement in flow:
                    if isinstance(movement, AmortFund):
                        flowModel.append(AmortFund.toModel(movement))
                    elif isinstance(movement, AmortDesemb):
                        flowModel.append(AmortDesemb.toModel(movement))
                return CashFlowModel(amorts=flowModel)
