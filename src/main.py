from typing import Any

import uvicorn

from src.adapters.excel.a_excel import AExcel
from src.controllers.fastapi.http.responses import *
from src.init import Init
from src.models.desemb import Desemb
from src.models.enums.config import *
from src.models.fund import Fund

if __name__ == '__main__':
    init = Init(_REPO_TYPE=REPO_TYPE.MOCK, _CTRL_TYPE=CTRL_TYPE.FASTAPI, _adapters=[ADAPTER.EXCEL.value])()
    repo = init[CONFIG.REPOSITORY_TYPE.value]
    ctrl = init[CONFIG.CONTROLLER_TYPE.value]
    excel: AExcel = init[CONFIG.ADAPTERS.value][ADAPTER.EXCEL.value]


    @ctrl.app.get('/', response_model=RootModel)
    async def root():
        return RootModel(
            repository_type=str(type(repo)),
            controller_type=str(type(ctrl)),
            adapters=[str(excel)]
        )


    @ctrl.app.get('/fund/all', response_model=dict[str, Any])
    async def getAllFunds():
        fundModels = ctrl.getAllFunds()
        funds = [Fund.fromModel(model) for model in fundModels]
        fundsFlat = excel.flattenFunds(funds)
        return fundsFlat


    @ctrl.app.get('/desemb/all', response_model=dict[str, Any])
    async def getAllDesembs():
        desembModels = ctrl.getAllDesembs()
        desembs = [Desemb.fromModel(model) for model in desembModels]
        desembsFlat = excel.flattenDesembs(desembs)
        return desembsFlat


    uvicorn.run(ctrl.app, host=ctrl.host, port=ctrl.port)

    pass
