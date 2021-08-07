from datetime import date

from src.models.desemb import Desemb
from src.models.enums.ccy import CCY
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

        assert desemb.pk == desembPk
        assert desemb.ccb == desembCcb
        assert desemb.ccy == desembCcy
        assert desemb.princ == desembPrinc
        assert desemb.ini == desembIni
        assert desemb.venc == desembVenc
        assert desemb.fund.pk == fundPk
        assert desemb.fund.kold == fundKold
        assert desemb.fund.ccy == fundCcy
        assert desemb.fund.princ == fundPrinc
        assert desemb.fund.ini == fundIni
        assert desemb.fund.venc == fundVenc

