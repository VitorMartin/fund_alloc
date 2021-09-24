import uvicorn

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


    @ctrl.app.get('/fund', response_model=FundsModel)
    async def getAllFunds():
        fundModels = [Fund.toModel(fund) for fund in ctrl.getAllFunds()]
        return FundsModel(funds=fundModels)


    @ctrl.app.get('/desemb', response_model=DesembsModel)
    async def getAllDesembs():
        desembModels = [Desemb.toModel(desemb) for desemb in ctrl.getAllDesembs()]
        return DesembsModel(desembs=desembModels)


    @ctrl.app.get('/amortFund', response_model=AmortFundsModel)
    async def getAllAmortFunds():
        amortFundModels = [AmortFund.toModel(amortFund) for amortFund in ctrl.getAllAmortFunds()]
        return AmortFundsModel(amortFunds=amortFundModels)


    @ctrl.app.get('/amortDesemb', response_model=AmortDesembsModel)
    async def getAllAmortDesembs():
        amortDesembModels = [AmortDesemb.toModel(amortDesemb) for amortDesemb in ctrl.getAllAmortDesembs()]
        return AmortDesembsModel(amortDesembs=amortDesembModels)


    @ctrl.app.get('/amortDesemb', response_model=AmortDesembsModel)
    async def getAllAmortDesembs():
        amortDesembModels = [AmortDesemb.toModel(amortDesemb) for amortDesemb in ctrl.getAllAmortDesembs()]
        return AmortDesembsModel(amortDesembs=amortDesembModels)


    uvicorn.run(ctrl.app, host=ctrl.host, port=ctrl.port)

    pass
