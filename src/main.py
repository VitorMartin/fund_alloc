import uvicorn

from adapters.excel.a_excel import AExcel
from controllers.fastapi.http.models import *
from controllers.fastapi.http.responses import *
from src.init import Init
from src.models.enums.config import *

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
            adapters=[str(type(excel))]
        )


    @ctrl.app.get('/fund/all', response_model=List[FundModel])
    async def getAllFunds():
        funds = ctrl.getAllFunds()
        return funds


    @ctrl.app.get('/desemb/all', response_model=List[DesembModel])
    async def getAllDesembs():
        desembs = ctrl.getAllDesembs()
        return desembs


    uvicorn.run(ctrl.app, host=ctrl.host, port=ctrl.port)

    pass
