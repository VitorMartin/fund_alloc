from fastapi import APIRouter

from src.controllers.fastapi.router.routes.amort_desemb_routes import AmortDesembRoutes
from src.controllers.fastapi.router.routes.amort_fund_routes import AmortFundRoutes
from src.controllers.fastapi.router.routes.desemb_routes import DesembRoutes
from src.controllers.fastapi.router.routes.fund_routes import FundRoutes
from src.controllers.fastapi.router.routes.root_routes import RootRoutes
from src.interfaces.i_c_storage import ICStorage
from src.interfaces.i_storage import IStorage


class Router(APIRouter):
    def __init__(self, repo: IStorage, ctrl: ICStorage, adapters: dict):
        super().__init__()

        self.include_router(RootRoutes(repo, ctrl, adapters))
        self.include_router(FundRoutes(ctrl))
        self.include_router(DesembRoutes(ctrl))
        self.include_router(AmortFundRoutes(ctrl))
        self.include_router(AmortDesembRoutes(ctrl))
