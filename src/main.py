import uvicorn

from src.controllers.fastapi.errors.errors import *
from src.controllers.fastapi.http.responses import *
from src.init import Init
from src.models.amort_desemb import AmortDesemb
from src.models.amort_fund import AmortFund
from src.models.desemb import Desemb
from src.models.enums.config import *
from src.models.enums.dict_keys import *
from src.models.fund import Fund

if __name__ == '__main__':
    init = Init(_REPO_TYPE=REPO_TYPE.MOCK, _CTRL_TYPE=CTRL_TYPE.FASTAPI)()
    repo = init[CONFIG.REPOSITORY_TYPE.value]
    ctrl = init[CONFIG.CONTROLLER_TYPE.value]
    adapters = init[CONFIG.ADAPTERS.value]


    @ctrl.app.get('/', response_model=RootModel)
    async def root():
        return RootModel(
            repository_type=str(type(repo)),
            controller_type=str(type(ctrl)),
            adapters=[str(type(ad)) for ad in adapters]
        )


    @ctrl.app.get('/fund', response_model=Union[FundsModel, FundModel])
    async def getAllFunds(dealId: int = None, kold: str = None):
        if dealId is None and kold is None:
            return FundsModel(funds=[Fund.toModel(fund) for fund in ctrl.getAllFunds()])
        elif dealId is not None and kold is None:
            return Fund.toModel(ctrl.getFundById(dealId))
        elif kold is not None and dealId is None:
            return Fund.toModel(ctrl.getFundByKold(kold))
        else:
            raise TooManyArgsException()


    @ctrl.app.get('/desemb', response_model=Union[DesembsModel, DesembModel])
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


    @ctrl.app.get('/amortFund', response_model=Union[AmortFundsModel, AmortFundModel])
    async def getAllAmortFunds(amortId: int = None, dealId: int = None):
        if amortId is None and dealId is None:
            return AmortFundsModel(amortFunds=[AmortFund.toModel(amortFund) for amortFund in ctrl.getAllAmortFunds()])
        elif amortId is not None and dealId is None:
            return AmortFund.toModel(ctrl.getAmortFundById(amortId))
        elif dealId is not None and amortId is None:
            return AmortFundsModel(
                amortFunds=[AmortFund.toModel(amortFund) for amortFund in ctrl.getAmortFundsByFundId(dealId)]
            )
        else:
            raise TooManyArgsException()


    @ctrl.app.get('/amortDesemb', response_model=Union[AmortDesembsModel, AmortDesembModel])
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


    @ctrl.app.get('/fund/princ', response_model=PrincModel)
    async def getFundPrincAfterAmort(dealId: int, basedate: date = None):
        if basedate is None:
            return PrincModel(princ=ctrl.getFundPrincAfterAmortById(dealId))
        else:
            return PrincModel(princ=ctrl.getFundPrincAfterAmortById(dealId, basedate))


    @ctrl.app.get('/desemb/princ', response_model=PrincModel)
    async def getDesembPrincAfterAmort(dealId: int, basedate: date = None):
        if basedate is None:
            return PrincModel(princ=ctrl.getDesembPrincAfterAmortById(dealId))
        else:
            return PrincModel(princ=ctrl.getDesembPrincAfterAmortById(dealId, basedate))


    @ctrl.app.get('/fund/availability', response_model=Union[FundsModel, FundAvailabilityModel])
    async def getAvailableFundsForDesembByCcb(ccb: str = None, basedate: date = None, kold: str = None):
        if kold is None:
            if ccb is None:
                raise MissingArgsException()
            else:
                if basedate is None:
                    return FundsModel(funds=[Fund.toModel(fund) for fund in ctrl.getAvailableFundsForDesembByCcb(ccb)])
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


    @ctrl.app.get('/fund/flow')
    async def generateFundFlowByKold(kold: str):
        flowModel = []
        flow = ctrl.generateFundFlowByKold(kold)
        for movement in flow:
            if isinstance(movement, AmortFund):
                flowModel.append(AmortFund.toModel(movement))
            elif isinstance(movement, AmortDesemb):
                flowModel.append(AmortDesemb.toModel(movement))
        return CashFlowModel(amorts=flowModel)


    uvicorn.run(ctrl.app, host=ctrl.host, port=ctrl.port)

    pass
