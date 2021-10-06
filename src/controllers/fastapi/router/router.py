from typing import List

from fastapi import APIRouter

from src.controllers.fastapi.router.routes.root_routes import RootRoutes
from src.interfaces.i_c_storage import ICStorage
from src.interfaces.i_storage import IStorage


class Router(APIRouter):
    def __init__(self, repo: IStorage, ctrl: ICStorage, adapters: List[str]):
        super().__init__()

        self.include_router(RootRoutes(repo, ctrl, adapters))
