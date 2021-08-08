import json

from src.models.enums.config import CONFIG
from src.repositories.access.storage_access import StorageAccess
from src.repositories.mock.storage_mock import StorageMock
from src.controllers.c_storage_func import CStorageFunc


class Init:
    def __call__(self, *args, **kwargs):
        with open(CONFIG.CONFIG_PATH.value) as file:
            data = json.load(file)
            repoType = data[CONFIG.REPOSITORY_TYPE.value]
            ctrlType = data[CONFIG.CONTROLLER_TYPE.value]

        # REPOSITORY TYPE #
        if repoType == CONFIG.MOCK.value:
            repo = StorageMock()
        elif repoType == CONFIG.ACCESS.value:
            repo = StorageAccess()
        else:
            raise Exception('Invalid repository type')

        # CONTROLLER TYPE #
        if ctrlType == CONFIG.FUNC.value:
            ctrl = CStorageFunc(repo)
        else:
            raise Exception('Invalid controller type')

        return repo, ctrl
