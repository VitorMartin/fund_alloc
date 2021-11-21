from fastapi import APIRouter

from src.controllers.fastapi.http.responses import RootModel
from src.interfaces.i_c_storage import ICStorage
from src.interfaces.i_storage import IStorage


class RootRoutes(APIRouter):
    def __init__(self, repo: IStorage, ctrl: ICStorage, adapters: dict):
        super().__init__(
            prefix=''
        )

        @self.get('/', response_model=RootModel)
        async def root():
            return RootModel(
                repository_type=str(type(repo)),
                controller_type=str(type(ctrl)),
                adapters=[str(adapter) for (_, adapter) in adapters.items()]
            )
