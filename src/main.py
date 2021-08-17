import uvicorn
from fastapi import FastAPI, Response

from src.controllers.fastapi.c_storage_fastapi import CStorageFastAPI
from src.models.enums.config import *
from src.init import Init

if __name__ == '__main__':
    ctrl: CStorageFastAPI = Init(_REPO_TYPE=REPO_TYPE.ACCESS, _CTRL_TYPE=CTRL_TYPE.FASTAPI)()
    app = FastAPI()

    @app.get('/')
    async def root():
        return Response('{"msg": "Hello FastAPI"}')


    @app.get('/fund/all')
    async def getAllFunds():
        return ctrl.getAllFunds()


    @app.get('/desemb/all')
    async def getAllDesembs():
        return ctrl.getAllDesembs()

    uvicorn.run(app, host='0.0.0.0', port=8000)

    pass
