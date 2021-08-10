from typing import List

from src.controllers.c_storage_func import CStorageFunc
from src.models.desemb import Desemb
from src.repositories.access.storage_access import StorageAccess
from src.repositories.mock.mock_data import MockData


class Test_UCGetDesembsInFund:
    def test_get_desembs_in_fund_by_kold(self):
        controller = CStorageFunc(StorageAccess())

        actualDesembs = controller.getDesembsInFundByKold('350151')
        expectedDesembs = [MockData.desemb4, MockData.desemb3, MockData.desemb2]

        assert isinstance(actualDesembs, List)
        assert [isinstance(desemb, Desemb) for desemb in actualDesembs]
        assert actualDesembs == expectedDesembs
