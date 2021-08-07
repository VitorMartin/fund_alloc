from datetime import date

from src.models.enums.ccy import CCY
from src.models.amort_fund import AmortFund
from src.models.fund import Fund


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

        assert amortFund.pk == amortPk
        assert amortFund.ccy == amortCcy
        assert amortFund.val == amortVal
        assert amortFund.date == amortDate
        assert amortFund.fund.pk == fundPk
        assert amortFund.fund.kold == fundKold
        assert amortFund.fund.ccy == fundCcy
        assert amortFund.fund.princ == fundPrinc
        assert amortFund.fund.ini == fundIni
        assert amortFund.fund.venc == fundVenc
