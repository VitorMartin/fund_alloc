from src.controllers.c_storage_func import CStorageFunc
from src.models.amort import Amort
from src.repositories.access.storage_access import StorageAccess
from src.repositories.mock.mock_data import MockData


class Test_UCgetValues:
    def test_get_remaining_principal_in_fund_by_id(self):
        controller = CStorageFunc(StorageAccess())

        fund = MockData.fund2
        actualFlow = controller.generateAmortsInFundByKold(fund.kold)
        expectedFlow = [
            MockData.amortFund3,
            MockData.amortFund4,
            MockData.amortFund5,
            MockData.amortFund6,
            MockData.amortFund7,
            MockData.amortDesemb3,
            MockData.amortDesemb4,
            MockData.amortDesemb5,
            MockData.amortDesemb6,
            MockData.amortDesemb7,
            MockData.amortDesemb8,
            MockData.amortDesemb9,
            MockData.amortDesemb10,
            MockData.amortDesemb11,
            MockData.amortDesemb12,
        ]
        expectedFlow.sort(key=lambda amort: amort.data)

        assert len(actualFlow) == len(expectedFlow)

        for i in range(len(actualFlow)):
            actualMovement = actualFlow[i]
            expectedMovement = expectedFlow[i]

            assert isinstance(actualMovement, Amort)
            assert actualMovement == expectedMovement
