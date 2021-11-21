from src.models.amort_desemb import AmortDesemb
from src.models.amort_fund import AmortFund
from src.models.desemb import Desemb
from src.models.fund import Fund
from src.repositories.mock.mock_data import MockData
from tests.ctrl import Ctrl


ctrl = Ctrl().ctrl


class Test_UCGetAll:
    def test_get_all_funds(self):
        actualFunds = sorted(ctrl.getAllFunds(), key=lambda fund: fund.dealId)
        expectedFunds = sorted(MockData.funds, key=lambda fund: fund.dealId, reverse=False)

        assert len(actualFunds) == len(expectedFunds)

        for i in range(len(actualFunds)):
            actualFund = actualFunds[i]
            expectedFund = expectedFunds[i]

            assert isinstance(actualFund, Fund)
            assert actualFund == expectedFund

    def test_get_all_desembs(self):
        actualDesembs = sorted(ctrl.getAllDesembs(), key=lambda fund: fund.dealId)
        expectedDesembs = sorted(MockData.desembs, key=lambda fund: fund.dealId)

        assert len(actualDesembs) == len(expectedDesembs)

        for i in range(len(actualDesembs)):
            actualDesemb = actualDesembs[i]
            expectedDesemb = expectedDesembs[i]

            assert isinstance(actualDesemb, Desemb)
            assert actualDesemb == expectedDesemb

    def test_get_all_amort_funds(self):
        actualAmortFunds = sorted(ctrl.getAllAmortFunds(), key=lambda amort: amort.amortId)
        expectedAmortFunds = sorted(MockData.amortFunds, key=lambda amort: amort.amortId)

        assert len(actualAmortFunds) == len(expectedAmortFunds)

        for i in range(len(actualAmortFunds)):
            actualAmortFund = actualAmortFunds[i]
            expectedAmortFund = expectedAmortFunds[i]

            assert isinstance(actualAmortFund, AmortFund)
            assert actualAmortFund == expectedAmortFund

    def test_get_all_amort_desembs(self):
        actualAmortDesembs = sorted(ctrl.getAllAmortDesembs(), key=lambda amort: amort.amortId)
        expectedAmortDesembs = sorted(MockData.amortDesembs, key=lambda amort: amort.amortId)

        assert len(actualAmortDesembs) == len(expectedAmortDesembs)

        for i in range(len(actualAmortDesembs)):
            actualAmortDesemb = actualAmortDesembs[i]
            expectedAmortDesemb = expectedAmortDesembs[i]

            assert isinstance(actualAmortDesemb, AmortDesemb)
            assert actualAmortDesemb == expectedAmortDesemb
