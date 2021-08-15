import json

from controllers.fastapi.c_storage_fastapi import CStorageFastAPI
from controllers.func.c_storage_func import CStorageFunc
from src.models.enums.config import *
from src.repositories.access.storage_access import StorageAccess
from src.repositories.mock.storage_mock import StorageMock


class Init:
    repoType: str
    ctrlType: str

    def __init__(self, _REPO_TYPE: REPO_TYPE = None, _CTRL_TYPE: CTRL_TYPE = None):
        with open(CONFIG.CONFIG_PATH.value) as file:
            data = json.load(file)
            if _REPO_TYPE is None:
                self.repoType = data[REPO_TYPE.REPOSITORY_TYPE.value]
            else:
                self.repoType = _REPO_TYPE.value

            if _CTRL_TYPE is None:
                self.ctrlType = data[CTRL_TYPE.CONTROLLER_TYPE.value]
            else:
                self.ctrlType = _CTRL_TYPE.value

            # REPOSITORY TYPE #
    def __call__(self, *args, **kwargs):
        if self.repoType == REPO_TYPE.MOCK.value:
            repo = StorageMock()
        elif self.repoType == REPO_TYPE.ACCESS.value:
            repo = StorageAccess()
        else:
            raise Exception('Invalid repository type')

        # CONTROLLER TYPE #
        if self.ctrlType == CTRL_TYPE.FUNC.value:
            ctrl = CStorageFunc(repo)
        elif self.ctrlType == CTRL_TYPE.FUNC.value:
            ctrl = CStorageFastAPI(repo)
        else:
            raise Exception('Invalid controller type')

        return ctrl
