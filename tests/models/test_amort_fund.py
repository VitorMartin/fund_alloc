from src.models.amort_fund import AmortFund
from src.models.enums.dict_keys import *
from src.models.fund import Fund
from src.repositories.mock.mock_data import MockData


class Test_AmortFund:
    def test_instance(self):
        amortFund = AmortFund(
            Fund(
                MockData.amortFund1.fund.kold,
                MockData.amortFund1.fund.ccy,
                MockData.amortFund1.fund.princ,
                MockData.amortFund1.fund.ini,
                MockData.amortFund1.fund.venc,
                pk=MockData.amortFund1.fund.dealId
            ),
            MockData.amortFund1.data,
            MockData.amortFund1.ccy,
            MockData.amortFund1.val,
            pk=MockData.amortFund1.amortId
        )

        assert isinstance(amortFund, AmortFund)
        assert amortFund == MockData.amortFund1

    def test_from_dict(self):
        d = {
            FUND.ID.value: MockData.amortFund1.fund.dealId,
            FUND.KOLD.value: MockData.amortFund1.fund.kold,
            FUND.CCY.value: MockData.amortFund1.fund.ccy,
            FUND.PRINC.value: MockData.amortFund1.fund.princ,
            FUND.INI.value: MockData.amortFund1.fund.ini,
            FUND.VENC.value: MockData.amortFund1.fund.venc,

            AMORT_FUND.ID.value: MockData.amortFund1.amortId,
            AMORT_FUND.CCY.value: MockData.amortFund1.ccy,
            AMORT_FUND.VAL.value: MockData.amortFund1.val,
            AMORT_FUND.DATA.value: MockData.amortFund1.data
        }

        amortFund = AmortFund.fromDict(d)

        assert isinstance(amortFund, AmortFund)
        assert amortFund == MockData.amortFund1
