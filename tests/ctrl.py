from src.controllers.fastapi.c_storage_fastapi import CStorageFastAPI
from src.interfaces.i_c_storage import ICStorage
from src.repositories.mock.storage_mock import StorageMock


class Ctrl:
    ctrl: ICStorage

    def __init__(self, ctrl: ICStorage = CStorageFastAPI(StorageMock(), autostart=False)):
        self.ctrl = ctrl
