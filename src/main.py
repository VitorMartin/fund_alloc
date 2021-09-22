import uvicorn
from fastapi import Response

from src.init import Init
from src.models.enums.config import *

if __name__ == '__main__':
    init = Init(_REPO_TYPE=REPO_TYPE.MOCK, _CTRL_TYPE=CTRL_TYPE.FASTAPI, _adapters=[ADAPTER.EXCEL.value])()
    repo = init[CONFIG.REPOSITORY_TYPE.value]
    ctrl = init[CONFIG.CONTROLLER_TYPE.value]
    excel = init[CONFIG.ADAPTERS.value][ADAPTER.EXCEL.value]


    @ctrl.app.get('/')
    async def root():
        return Response(
            '{'
            f'"repo": "{type(repo)}",'
            f'"ctrl": "{type(ctrl)}",'
            f'"adapters": "[{type(excel)}]"'
            '}'
        )

    @ctrl.app.get('/fund/all')
    async def getAllFunds():
        return ctrl.getAllFunds()

    @ctrl.app.get('/desemb/all')
    async def getAllDesembs():
        return ctrl.getAllDesembs()

    uvicorn.run(ctrl.app, host=ctrl.host, port=ctrl.port)

    pass
