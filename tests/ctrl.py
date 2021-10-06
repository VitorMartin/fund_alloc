from src.controllers.fastapi.c_storage_fastapi import CStorageFastAPI
from src.interfaces.i_c_storage import ICStorage
from src.repositories.access.storage_access import StorageAccess


class Ctrl:
    ctrl: ICStorage

    def __init__(self, ctrl: ICStorage = CStorageFastAPI(StorageAccess(), autostart=False)):
        self.ctrl = ctrl
