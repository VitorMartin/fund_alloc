from datetime import date

from src.models.desemb import Desemb
from src.models.enums.ccy import CCY
from src.models.enums.dict_keys import *
from src.models.fund import Fund
from src.repositories.mock.mock_data import MockData


class Test_Desemb:
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

        assert type(desemb) is Desemb

        assert desemb.dealId == desembPk
        assert desemb.ccb == desembCcb
        assert desemb.ccy == desembCcy
        assert desemb.princ == desembPrinc
        assert desemb.ini == desembIni
        assert desemb.venc == desembVenc
        assert desemb.fund.dealId == fundPk
        assert desemb.fund.kold == fundKold
        assert desemb.fund.ccy == fundCcy
        assert desemb.fund.princ == fundPrinc
        assert desemb.fund.ini == fundIni
        assert desemb.fund.venc == fundVenc

    def test_from_dict(self):
        d = {
            FUND.ID.value: MockData.desemb1.fund.dealId,
            FUND.KOLD.value: MockData.desemb1.fund.kold,
            FUND.CCY.value: MockData.desemb1.fund.ccy,
            FUND.PRINC.value: MockData.desemb1.fund.princ,
            FUND.INI.value: MockData.desemb1.fund.ini,
            FUND.VENC.value: MockData.desemb1.fund.venc,

            DESEMB.ID.value: MockData.desemb1.dealId,
            DESEMB.CCB.value: MockData.desemb1.ccb,
            DESEMB.CCY.value: MockData.desemb1.ccy,
            DESEMB.PRINC.value: MockData.desemb1.princ,
            DESEMB.INI.value: MockData.desemb1.ini,
            DESEMB.VENC.value: MockData.desemb1.venc
        }

        desemb = Desemb.fromDict(d)

        assert type(desemb) is Desemb

        assert desemb.fund.dealId == MockData.desemb1.fund.dealId
        assert desemb.fund.kold == MockData.desemb1.fund.kold
        assert desemb.fund.ccy == MockData.desemb1.fund.ccy
        assert desemb.fund.princ == MockData.desemb1.fund.princ
        assert desemb.fund.ini == MockData.desemb1.fund.ini
        assert desemb.fund.venc == MockData.desemb1.fund.venc

        assert desemb.dealId == MockData.desemb1.dealId
        assert desemb.ccb == MockData.desemb1.ccb
        assert desemb.ccy == MockData.desemb1.ccy
        assert desemb.princ == MockData.desemb1.princ
        assert desemb.ini == MockData.desemb1.ini
        assert desemb.venc == MockData.desemb1.venc
