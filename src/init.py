import json
import os
from typing import Any, List

from src.adapters.excel.a_excel import AExcel
from src.controllers.fastapi.c_storage_fastapi import CStorageFastAPI
from src.controllers.func.c_storage_func import CStorageFunc
from src.models.enums.config import *
from src.repositories.access.storage_access import StorageAccess
from src.repositories.mock.storage_mock import StorageMock


class Init:
    repoType: str
    ctrlType: str
    adaptersList: List[str]
    adapters: List[Any]
    rootPath: str
    configPath: str

    def __init__(
            self, _REPO_TYPE: REPO_TYPE = None, _CTRL_TYPE: CTRL_TYPE = None, _adaptersList: List[str] = None
    ):
        self.rootPath = os.path.dirname(__file__)
        self.configPath = os.path.join(self.rootPath, CONFIG.CONFIG_FILENAME.value)
        with open(self.configPath) as file:
            deployConfig = json.load(file)

        if _REPO_TYPE is None:
            self.repoType = deployConfig[REPO_TYPE.REPOSITORY_TYPE.value]
        else:
            self.repoType = _REPO_TYPE.value

        if _CTRL_TYPE is None:
            self.ctrlType = deployConfig[CTRL_TYPE.CONTROLLER_TYPE.value]
        else:
            self.ctrlType = _CTRL_TYPE.value

        self.adapters = []
        if _adaptersList is None:
            self.adaptersList = deployConfig[CONFIG.ADAPTERS.value]
        else:
            self.adaptersList = _adaptersList

    def __call__(self, *args, **kwargs):
        configDict = {}

        # REPOSITORY TYPE #
        if self.repoType == REPO_TYPE.MOCK.value:
            repo = StorageMock()
        elif self.repoType == REPO_TYPE.ACCESS.value:
            repo = StorageAccess()
        else:
            raise Exception('Invalid repository type')
        configDict[CONFIG.REPOSITORY_TYPE.value] = repo

        # ADAPTERS #
        configDict[CONFIG.ADAPTERS.value] = {}
        for adapter in self.adaptersList:
            if adapter == ADAPTER.EXCEL.value:
                self.adapters.append(AExcel)
                configDict[CONFIG.ADAPTERS.value][ADAPTER.EXCEL.value] = AExcel

        # CONTROLLER TYPE #
        if self.ctrlType == CTRL_TYPE.FUNC.value:
            ctrl = CStorageFunc(repo)
        elif self.ctrlType == CTRL_TYPE.FASTAPI.value:
            ctrl = CStorageFastAPI(repo, self.adapters)
        else:
            raise Exception('Invalid controller type')
        configDict[CONFIG.CONTROLLER_TYPE.value] = ctrl

        return configDict
