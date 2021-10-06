from fastapi import APIRouter

from src.controllers.fastapi.errors.errors import *
from src.controllers.fastapi.http.responses import *
from src.interfaces.i_c_storage import ICStorage
from src.models.amort_desemb import AmortDesemb
from src.models.amort_fund import AmortFund
from src.models.desemb import Desemb
from src.models.enums.dict_keys import FLOW_CHANGE
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

        @self.get('/amorts', response_model=CashFlowModel)
        async def getAmortsInFundByKold(kold: str = None):
            if kold is None:
                raise MissingArgsException()
            else:
                flowModel = []
                flow = ctrl.getAmortsInFundByKold(kold)
                for movement in flow:
                    if isinstance(movement, AmortFund):
                        flowModel.append(AmortFund.toModel(movement))
                    elif isinstance(movement, AmortDesemb):
                        flowModel.append(AmortDesemb.toModel(movement))
                return CashFlowModel(amorts=flowModel)

        @self.get('/flow', response_model=FlowModel)
        async def generateFundFlowByKold(kold: str = None):
            if kold is None:
                raise MissingArgsException()
            else:
                flowModel = []
                flow = ctrl.generateFundFlowByKold(kold)
                for flowChange in flow:
                    if isinstance(flowChange[FLOW_CHANGE.OP.value], Fund):
                        opModel = Fund.toModel(flowChange[FLOW_CHANGE.OP.value])
                    elif isinstance(flowChange[FLOW_CHANGE.OP.value], Desemb):
                        opModel = Desemb.toModel(flowChange[FLOW_CHANGE.OP.value])
                    elif isinstance(flowChange[FLOW_CHANGE.OP.value], AmortFund):
                        opModel = AmortFund.toModel(flowChange[FLOW_CHANGE.OP.value])
                    elif isinstance(flowChange[FLOW_CHANGE.OP.value], AmortDesemb):
                        opModel = AmortDesemb.toModel(flowChange[FLOW_CHANGE.OP.value])
                    else:
                        raise InternalServerError()

                    flowModel.append(FlowChangeModel(
                        op=opModel,
                        type=flowChange[FLOW_CHANGE.TYPE.value],
                        data=flowChange[FLOW_CHANGE.DATA.value],
                        val=flowChange[FLOW_CHANGE.VAL.value],
                        fundPrinc=flowChange[FLOW_CHANGE.FUND_PRINC.value],
                        desembPrinc=flowChange[FLOW_CHANGE.DESEMB_PRINC.value],
                        availBefore=flowChange[FLOW_CHANGE.AVAIL_BEFORE.value],
                        availAfter=flowChange[FLOW_CHANGE.AVAIL_AFTER.value]
                    ))
                return FlowModel(flow=flowModel)
