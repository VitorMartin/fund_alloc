from src.interfaces.i_storage import IStorage


class UCGetAllFunds:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self):
        return self.storage.getAllFunds()


class UCGetAllDesembs:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self):
        return self.storage.getAllDesembs()


class UCGetAllAmortFunds:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self):
        return self.storage.getAllAmortFunds()


class UCGetAllAmortDesembs:
    storage: IStorage

    def __init__(self, storageRepo: IStorage):
        self.storage = storageRepo

    def __call__(self):
        return self.storage.getAllAmortDesembs()
