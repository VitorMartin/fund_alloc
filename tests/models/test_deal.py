from datetime import date

from src.models.deal import Deal
from src.models.enums.ccy import CCY


class Test_Deal:
    def test_instance(self):
        pk = 1
        ccy = CCY.USD
        princ = 500.66
        ini = date(2020, 1, 30)
        venc = date(2020, 12, 30)

        deal = Deal(ccy, princ, ini, venc, pk=pk)

        assert type(deal) is Deal

        assert deal.pk == pk
        assert deal.ccy == ccy
        assert deal.princ == princ
        assert deal.ini == ini
        assert deal.venc == venc
