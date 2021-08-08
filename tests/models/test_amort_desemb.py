from datetime import date

from src.models.enums.ccy import CCY
from src.models.amort_desemb import AmortDesemb
from src.models.fund import Fund
from src.models.desemb import Desemb


class Test_AmortDesemb:
    def test_instance(self):
        fundPk = 1
        fundKold = '111111'
        fundCcy = CCY.USD
        fundPrinc = 1150.25
        fundIni = date(2020, 1, 30)
        fundVenc = date(2023, 12, 30)
        fund = Fund(fundKold, fundCcy, fundPrinc, fundIni, fundVenc, pk=fundPk)

        desembPk = 2
        desembCcb = '222222'
        desembCcy = CCY.USD
        desembPrinc = 838.10
        desembIni = date(2021, 1, 30)
        desembVenc = date(2022, 12, 30)
        desemb = Desemb(fund, desembCcb, desembCcy, desembPrinc, desembIni, desembVenc, pk=desembPk)

        amortPk = 3
        amortCcy = CCY.USD
        amortVal = 303.50
        amortDate = date(2021, 6, 30)
        amortDesemb = AmortDesemb(desemb, amortDate, amortCcy, amortVal, pk=amortPk)

        assert type(amortDesemb) is AmortDesemb

        assert amortDesemb.amortId == amortPk
        assert amortDesemb.ccy == amortCcy
        assert amortDesemb.val == amortVal
        assert amortDesemb.data == amortDate

        assert amortDesemb.desemb.dealId == desembPk
        assert amortDesemb.desemb.ccb == desembCcb
        assert amortDesemb.desemb.ccy == desembCcy
        assert amortDesemb.desemb.princ == desembPrinc
        assert amortDesemb.desemb.ini == desembIni
        assert amortDesemb.desemb.venc == desembVenc

        assert amortDesemb.desemb.fund.dealId == fundPk
        assert amortDesemb.desemb.fund.kold == fundKold
        assert amortDesemb.desemb.fund.ccy == fundCcy
        assert amortDesemb.desemb.fund.princ == fundPrinc
        assert amortDesemb.desemb.fund.ini == fundIni
        assert amortDesemb.desemb.fund.venc == fundVenc
