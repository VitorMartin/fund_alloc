from copy import copy

import pytest

from src.controllers.c_storage_func import CStorageFunc
from src.models.amort_desemb import AmortDesemb
from src.models.amort_fund import AmortFund
from src.models.desemb import Desemb
from src.models.enums.dict_keys import MODEL
from src.models.fund import Fund
from src.repositories.access.storage_access import StorageAccess
from src.repositories.mock.mock_data import MockData


class Test_UCGetOpByAttr:
    def test_get_fund_by_id(self):
        controller = CStorageFunc(StorageAccess())

        fund = controller.getFundById(MockData.fund1.dealId)

        assert isinstance(fund, Fund)

        assert fund.__dict__ == MockData.fund1.__dict__

    def test_get_desemb_by_id(self):
        controller = CStorageFunc(StorageAccess())

        desemb = copy(controller.getDesembById(MockData.desemb1.dealId))

        dActualDesemb = desemb.__dict__
        dActualFund = dActualDesemb.pop(MODEL.FUND.value).__dict__

        dExpectedDesemb = copy(MockData.desemb1).__dict__
        dExpectedFund = dExpectedDesemb.pop(MODEL.FUND.value).__dict__

        assert isinstance(desemb, Desemb)

        assert dActualDesemb.__str__() == dExpectedDesemb.__str__()
        assert dActualFund.__str__() == dExpectedFund.__str__()

    def test_get_amort_fund_by_id(self):
        controller = CStorageFunc(StorageAccess())

        amortFund = copy(controller.getAmortFundById(MockData.amortFund1.amortId))

        dActualAmortFund = amortFund.__dict__
        dActualFund = dActualAmortFund.pop(MODEL.FUND.value).__dict__

        dExpectedAmortFund = copy(MockData.amortFund1).__dict__
        dExpectedFund = dExpectedAmortFund.pop(MODEL.FUND.value).__dict__

        assert isinstance(amortFund, AmortFund)

        assert dActualAmortFund.__str__() == dExpectedAmortFund.__str__()
        assert dActualFund.__str__() == dExpectedFund.__str__()

    def test_get_amort_desemb_by_id(self):
        controller = CStorageFunc(StorageAccess())

        amortDesemb = copy(controller.getAmortDesembById(MockData.amortDesemb3.amortId))

        dActualAmortDesemb = amortDesemb.__dict__
        dActualDesemb = dActualAmortDesemb.pop(MODEL.DESEMB.value).__dict__
        dActualFund = dActualDesemb.pop(MODEL.FUND.value).__dict__

        dExpectedAmortDesemb = copy(MockData.amortDesemb3).__dict__
        dExpectedDesemb = dExpectedAmortDesemb.pop(MODEL.DESEMB.value).__dict__
        dExpectedFund = dExpectedDesemb.pop(MODEL.FUND.value).__dict__

        assert isinstance(amortDesemb, AmortDesemb)

        assert dActualAmortDesemb.__str__() == dExpectedAmortDesemb.__str__()
        assert dActualDesemb.__str__() == dExpectedDesemb.__str__()
        assert dActualFund.__str__() == dExpectedFund.__str__()
