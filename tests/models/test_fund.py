from datetime import date

from src.models.fund import Fund
from src.models.enums.ccy import CCY


class Test_Fund:
    def test_instance(self):
        pk = 1
        kold = '111111'
        ccy = CCY.USD
        princ = 500.66
        ini = date(2020, 1, 30)
        venc = date(2020, 12, 30)

        fund = Fund(kold, ccy, princ, ini, venc, pk=pk)

        assert type(fund) is Fund

        assert fund.dealId == pk
        assert fund.kold == kold
        assert fund.ccy == ccy
        assert fund.princ == princ
        assert fund.ini == ini
        assert fund.venc == venc
