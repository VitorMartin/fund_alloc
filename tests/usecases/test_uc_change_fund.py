import pytest

from ctrl import Ctrl
from src.repositories.mock.mock_data import MockData
from src.usecases.errors.ccy_break_error import CcyBreakError
from src.usecases.errors.date_break_error import DateBreakError
from src.usecases.errors.value_break_error import ValueBreakError

ctrl = Ctrl().ctrl


class Test_UCChangeFund:
    def test_change_fund(self):
        desemb = MockData.desemb1
        desemb.princ = 1
        newFund = MockData.fund2

        assert ctrl.getDesembById(desemb.dealId).fund.kold == desemb.fund.kold
        assert ctrl.changeFund(desemb, newFund)
        assert ctrl.getDesembById(desemb.dealId).fund.kold == newFund.kold

    def test_raise_ccy_break_error(self):
        desemb = MockData.desemb2
        newFund = MockData.fund3

        assert ctrl.getDesembById(desemb.dealId).fund.kold == desemb.fund.kold
        with pytest.raises(CcyBreakError):
            ctrl.changeFund(desemb, newFund)

    def test_raise_value_break_error(self):
        desemb = MockData.desemb3
        newFund = MockData.fund1

        assert ctrl.getDesembById(desemb.dealId).fund.kold == desemb.fund.kold
        with pytest.raises(ValueBreakError):
            ctrl.changeFund(desemb, newFund)

    def test_raise_date_break_error(self):
        desemb = MockData.desemb6
        desemb.princ = 1
        newFund = MockData.fund3

        assert ctrl.getDesembById(desemb.dealId).fund.kold == desemb.fund.kold
        with pytest.raises(DateBreakError):
            ctrl.changeFund(desemb, newFund)
