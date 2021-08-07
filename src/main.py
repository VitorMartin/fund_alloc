from src.repositories.mock.storage_mock import StorageMock
from src.controllers.c_storage_func import CStorageFunc


if __name__ == '__main__':
    repo = StorageMock()
    ctrl = CStorageFunc(repo)

    for fund in ctrl.getAllFunds():
        print(fund)
    print()
    for desemb in ctrl.getAllDesembs():
        print(desemb)
    print()
    for amortFund in ctrl.getAllAmortFunds():
        print(amortFund)
    print()
    for amortDesemb in ctrl.getAllAmortDesembs():
        print(amortDesemb)
