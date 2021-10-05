from ctrl import Ctrl
from src.repositories.mock.mock_data import MockData

ctrl = Ctrl().ctrl


class Test_UCChangeFund:
    def test_change_fund(self):
        desemb = MockData.desemb1
        newFund = MockData.fund2

        assert ctrl.getDesembById(desemb.dealId).fund.kold == '350150'
        assert ctrl.changeFund(desemb, newFund)
        assert ctrl.getDesembById(desemb.dealId).fund.kold == '350151'
