from src.controllers.fastapi.c_storage_fastapi import CStorageFastAPI
from src.interfaces.i_c_storage import ICStorage
from src.repositories.mock.storage_mock import StorageMock
from src.repositories.access.storage_access import StorageAccess
from src.interfaces.i_storage import IStorage


class Ctrl:
    ctrl: ICStorage

    def __init__(self, ctrl: ICStorage = CStorageFastAPI(StorageMock(), autostart=False)):
        self.ctrl = ctrl

    @staticmethod
    def ctrlEmptyRepo():
        return CStorageFastAPI(StorageMock(funds=[], desembs=[], amortFunds=[], amortDesembs=[]), autostart=False)
