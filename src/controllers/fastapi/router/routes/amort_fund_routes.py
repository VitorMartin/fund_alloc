from fastapi import APIRouter

from src.controllers.fastapi.errors.errors import *
from src.controllers.fastapi.http.responses import *
from src.interfaces.i_c_storage import ICStorage
from src.models.amort_fund import AmortFund


class AmortFundRoutes(APIRouter):
    def __init__(self, ctrl: ICStorage):
        super(AmortFundRoutes, self).__init__(
            prefix='/amort_fund'
        )

        @self.get('/', response_model=Union[AmortFundsModel, AmortFundModel])
        async def getAllAmortFunds(amortId: int = None, dealId: int = None):
            if amortId is None and dealId is None:
                return AmortFundsModel(
                    amortFunds=[AmortFund.toModel(amortFund) for amortFund in ctrl.getAllAmortFunds()])
            elif amortId is not None and dealId is None:
                return AmortFund.toModel(ctrl.getAmortFundById(amortId))
            elif dealId is not None and amortId is None:
                return AmortFundsModel(
                    amortFunds=[AmortFund.toModel(amortFund) for amortFund in ctrl.getAmortFundsByFundId(dealId)]
                )
            else:
                raise TooManyArgsException()
