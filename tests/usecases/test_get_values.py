from src.controllers.c_storage_func import CStorageFunc
from src.repositories.access.storage_access import StorageAccess
from src.repositories.mock.mock_data import MockData


class Test_UCgetValues:
    def test_get_remaining_principal_in_fund_by_id(self):
        controller = CStorageFunc(StorageAccess())

        remain = controller.getRemainPrincInFundById(MockData.fund2.dealId)

        assert isinstance(remain, float)
        assert remain == 16_000_000.
        