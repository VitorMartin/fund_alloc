from datetime import date

from src.models.enums.ccy import CCY
from src.models.enums.dict_keys import *
from src.models.amort_fund import AmortFund
from src.models.fund import Fund
from src.repositories.mock.mock_data import MockData


class Test_AmortFund:
    def test_instance(self):
        fundPk = 1
        fundKold = '111111'
        fundCcy = CCY.EUR
        fundPrinc = 654.20
        fundIni = date(2020, 1, 1)
        fundVenc = date(2022, 1, 1)
        fund = Fund(fundKold, fundCcy, fundPrinc, fundIni, fundVenc, pk=fundPk)

        amortPk = 2
        amortCcy = CCY.USD
        amortVal = 303.50
        amortDate = date(2021, 1, 1)
        amortFund = AmortFund(fund, amortDate, amortCcy, amortVal, pk=amortPk)

        assert type(amortFund) is AmortFund

        assert amortFund.amortId == amortPk
        assert amortFund.ccy == amortCcy
        assert amortFund.val == amortVal
        assert amortFund.data == amortDate
        assert amortFund.fund.dealId == fundPk
        assert amortFund.fund.kold == fundKold
        assert amortFund.fund.ccy == fundCcy
        assert amortFund.fund.princ == fundPrinc
        assert amortFund.fund.ini == fundIni
        assert amortFund.fund.venc == fundVenc

    def test_from_dict(self):
        d = {
            FUND.ID.value: MockData.amortDesemb1.desemb.fund.dealId,
            FUND.KOLD.value: MockData.amortDesemb1.desemb.fund.kold,
            FUND.CCY.value: MockData.amortDesemb1.desemb.fund.ccy,
            FUND.PRINC.value: MockData.amortDesemb1.desemb.fund.princ,
            FUND.INI.value: MockData.amortDesemb1.desemb.fund.ini,
            FUND.VENC.value: MockData.amortDesemb1.desemb.fund.venc,

            AMORT_FUND.ID.value: MockData.amortFund1.amortId,
            AMORT_FUND.CCY.value: MockData.amortFund1.ccy,
            AMORT_FUND.VAL.value: MockData.amortFund1.val,
            AMORT_FUND.DATA.value: MockData.amortFund1.data
        }

        amortFund = AmortFund.fromDict(d)

        assert type(amortFund) is AmortFund

        assert amortFund.fund.dealId == MockData.amortFund1.fund.dealId
        assert amortFund.fund.kold == MockData.amortFund1.fund.kold
        assert amortFund.fund.ccy == MockData.amortFund1.fund.ccy
        assert amortFund.fund.princ == MockData.amortFund1.fund.princ
        assert amortFund.fund.ini == MockData.amortFund1.fund.ini
        assert amortFund.fund.venc == MockData.amortFund1.fund.venc

        assert amortFund.amortId == MockData.amortFund1.amortId
        assert amortFund.ccy == MockData.amortFund1.ccy
        assert amortFund.data == MockData.amortFund1.data
        assert amortFund.val == MockData.amortFund1.val
