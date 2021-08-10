from src.controllers.c_storage_func import CStorageFunc
from src.repositories.mock.mock_data import MockData
from src.repositories.mock.storage_mock import StorageMock


class Test_UCGetAll:
    def test_get_all_funds(self):
        controller = CStorageFunc(StorageMock())

        assert controller.getAllFunds() == MockData.funds

    def test_get_all_desembs(self):
        controller = CStorageFunc(StorageMock())

        assert controller.getAllDesembs() == MockData.desembs

    def test_get_all_amort_funds(self):
        controller = CStorageFunc(StorageMock())

        assert controller.getAllAmortFunds() == MockData.amortFunds

    def test_get_all_amort_desembs(self):
        controller = CStorageFunc(StorageMock())

        assert controller.getAllAmortDesembs() == MockData.amortDesembs

