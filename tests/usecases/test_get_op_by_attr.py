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

    def test_get_amort_desemb_by_id(self):
        controller = CStorageFunc(StorageAccess())

        amortDesemb = controller.getAmortDesembById(MockData.amortDesemb1.amortId)

        assert isinstance(amortDesemb, AmortDesemb)
        assert amortDesemb == MockData.amortDesemb1
