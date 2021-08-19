import uvicorn
from fastapi import FastAPI, Response

from src.controllers.fastapi.c_storage_fastapi import CStorageFastAPI
from src.models.enums.config import *
from src.init import Init

if __name__ == '__main__':
    ctrl: CStorageFastAPI = Init(_REPO_TYPE=REPO_TYPE.ACCESS, _CTRL_TYPE=CTRL_TYPE.FASTAPI)()

    @ctrl.app.get('/')
    async def root():
        return Response('{"msg": "Hello from FastAPI!"}')


    @ctrl.app.get('/fund/all')
    async def getAllFunds():
        return ctrl.getAllFunds()


    @ctrl.app.get('/desemb/all')
    async def getAllDesembs():
        return ctrl.getAllDesembs()

    uvicorn.run(ctrl.app, host=ctrl.host, port=ctrl.port)

    pass
