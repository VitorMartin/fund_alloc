from src.controllers.c_storage_func import CStorageFunc
from src.repositories.access.storage_access import StorageAccess
from src.repositories.mock.mock_data import MockData


class Test_UCGetDesembsInFund:
    def test_get_desembs_in_fund_by_kold(self):
        controller = CStorageFunc(StorageAccess())

        actual = controller.getDesembsInFundByKold('350151')
        expected = [MockData.desemb4, MockData.desemb3, MockData.desemb2]

        assert len(actual) == len(expected)

        for i in range(len(actual)):
            assert actual[i].__str__() == expected[i].__str__()
