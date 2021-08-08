from datetime import date

from src.models.enums.ccy import CCY
from src.models.amort_desemb import AmortDesemb
from src.models.enums.dict_keys import *
from src.models.fund import Fund
from src.models.desemb import Desemb
from src.repositories.mock.mock_data import MockData


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

    def test_from_dict(self):
        d = {
            FUND.ID.value: MockData.amortDesemb1.desemb.fund.dealId,
            FUND.KOLD.value: MockData.amortDesemb1.desemb.fund.kold,
            FUND.CCY.value: MockData.amortDesemb1.desemb.fund.ccy,
            FUND.PRINC.value: MockData.amortDesemb1.desemb.fund.princ,
            FUND.INI.value: MockData.amortDesemb1.desemb.fund.ini,
            FUND.VENC.value: MockData.amortDesemb1.desemb.fund.venc,

            DESEMB.ID.value: MockData.amortDesemb1.desemb.dealId,
            DESEMB.CCB.value: MockData.amortDesemb1.desemb.ccb,
            DESEMB.INI.value: MockData.amortDesemb1.desemb.ini,
            DESEMB.CCY.value: MockData.amortDesemb1.desemb.ccy,
            DESEMB.PRINC.value: MockData.amortDesemb1.desemb.princ,
            DESEMB.VENC.value: MockData.amortDesemb1.desemb.venc,

            AMORT_DESEMB.ID.value: MockData.amortDesemb1.amortId,
            AMORT_DESEMB.CCY.value: MockData.amortDesemb1.ccy,
            AMORT_DESEMB.VAL.value: MockData.amortDesemb1.val,
            AMORT_DESEMB.DATA.value: MockData.amortDesemb1.data
        }

        amortDesemb = AmortDesemb.fromDict(d)

        assert type(amortDesemb) is AmortDesemb

        assert amortDesemb.desemb.fund.dealId == MockData.amortDesemb1.desemb.fund.dealId
        assert amortDesemb.desemb.fund.kold == MockData.amortDesemb1.desemb.fund.kold
        assert amortDesemb.desemb.fund.ccy == MockData.amortDesemb1.desemb.fund.ccy
        assert amortDesemb.desemb.fund.princ == MockData.amortDesemb1.desemb.fund.princ
        assert amortDesemb.desemb.fund.ini == MockData.amortDesemb1.desemb.fund.ini
        assert amortDesemb.desemb.fund.venc == MockData.amortDesemb1.desemb.fund.venc

        assert amortDesemb.desemb.dealId == MockData.amortDesemb1.desemb.dealId
        assert amortDesemb.desemb.ccb == MockData.amortDesemb1.desemb.ccb
        assert amortDesemb.desemb.ccy == MockData.amortDesemb1.desemb.ccy
        assert amortDesemb.desemb.princ == MockData.amortDesemb1.desemb.princ
        assert amortDesemb.desemb.ini == MockData.amortDesemb1.desemb.ini
        assert amortDesemb.desemb.venc == MockData.amortDesemb1.desemb.venc

        assert amortDesemb.amortId == MockData.amortDesemb1.amortId
        assert amortDesemb.ccy == MockData.amortDesemb1.ccy
        assert amortDesemb.data == MockData.amortDesemb1.data
        assert amortDesemb.val == MockData.amortDesemb1.val
