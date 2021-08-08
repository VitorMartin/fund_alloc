from datetime import date

from src.models.enums.ccy import CCY
from src.models.amort import Amort


class Test_Amort:
    def test_instance(self):
        pk = 1
        ccy = CCY.USD
        val = 500.66
        data = date(2020, 1, 30)

        amort = Amort(data, ccy, val, pk=pk)

        assert type(amort) is Amort

        assert amort.amortId == pk
        assert amort.data == data
        assert amort.ccy == ccy
        assert amort.val == val
