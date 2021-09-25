from typing import Union

import uvicorn

from src.controllers.fastapi.errors.too_many_args_exception import TooManyArgsException
from src.controllers.fastapi.http.responses import *
from src.init import Init
from src.models.amort_desemb import AmortDesemb
from src.models.amort_fund import AmortFund
from src.models.desemb import Desemb
from src.models.enums.config import *
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


    uvicorn.run(ctrl.app, host=ctrl.host, port=ctrl.port)

    pass
