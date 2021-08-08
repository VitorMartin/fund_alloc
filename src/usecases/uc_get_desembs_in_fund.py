from src.interfaces.i_storage import IStorage


class UCGetDesembsInFundByKold:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self, kold: str):
        return self.storage.getDesembsInFundByKold(kold)
