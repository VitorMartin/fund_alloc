import uvicorn
from fastapi import Response

from controllers.excel.c_storage_excel import CStorageExcel
from src.models.enums.config import *
from src.init import Init

if __name__ == '__main__':
    ctrl: CStorageExcel = Init(_REPO_TYPE=REPO_TYPE.MOCK, _CTRL_TYPE=CTRL_TYPE.EXCEL)()

    @ctrl.app.get('/')
    async def root():
        return Response('{"msg": "Hello from Excel!"}')


    @ctrl.app.get('/fund/all')
    async def getAllFunds():
        return ctrl.getAllFunds()


    @ctrl.app.get('/desemb/all')
    async def getAllDesembs():
        return ctrl.getAllDesembs()

    uvicorn.run(ctrl.app, host=ctrl.host, port=ctrl.port)

    pass
