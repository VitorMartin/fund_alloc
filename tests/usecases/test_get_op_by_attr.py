from src.controllers.c_storage_func import CStorageFunc
from src.models.amort_desemb import AmortDesemb
from src.models.amort_fund import AmortFund
from src.models.desemb import Desemb
from src.models.fund import Fund
from src.repositories.access.storage_access import StorageAccess
from src.repositories.mock.mock_data import MockData


class Test_UCGetOpByAttr:
    def test_get_fund_by_id(self):
        controller = CStorageFunc(StorageAccess())

        fund = controller.getFundById(MockData.fund1.dealId)

        assert isinstance(fund, Fund)
        assert fund == MockData.fund1

    def test_get_fund_by_kold(self):
        controller = CStorageFunc(StorageAccess())

        fund = controller.getFundByKold(MockData.fund1.kold)

        assert isinstance(fund, Fund)
        assert fund == MockData.fund1

    def test_get_desemb_by_id(self):
        controller = CStorageFunc(StorageAccess())

        desemb = controller.getDesembById(MockData.desemb1.dealId)

        assert isinstance(desemb, Desemb)
        assert desemb == MockData.desemb1

    def test_get_amort_fund_by_id(self):
        controller = CStorageFunc(StorageAccess())

        amortFund = controller.getAmortFundById(MockData.amortFund1.amortId)

        assert isinstance(amortFund, AmortFund)
        assert amortFund == MockData.amortFund1

    def test_get_amort_funds_by_fund_id(self):
        controller = CStorageFunc(StorageAccess())

        actualAmorts = controller.getAmortFundsByFundId(MockData.fund2.dealId)
        actualAmorts.sort(key=lambda amort: amort.amortId, reverse=False) # https://stackoverflow.com/questions/403421/how-to-sort-a-list-of-objects-based-on-an-attribute-of-the-objects

        expectedAmorts = [
            MockData.amortFund3,
            MockData.amortFund4,
            MockData.amortFund5,
            MockData.amortFund6,
            MockData.amortFund7
        ]

        for i in range(len(actualAmorts)):
            actualAmort = actualAmorts[i]
            expectedAmort = expectedAmorts[i]

            assert isinstance(actualAmort, AmortFund)
            assert actualAmort == expectedAmort

    def test_get_amort_desemb_by_id(self):
        controller = CStorageFunc(StorageAccess())

        amortDesemb = controller.getAmortDesembById(MockData.amortDesemb1.amortId)

        assert isinstance(amortDesemb, AmortDesemb)
        assert amortDesemb == MockData.amortDesemb1
