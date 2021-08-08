from datetime import date

from src.models.enums.ccy import CCY
from src.models.enums.dict_keys import *
from src.models.amort import Amort
from src.repositories.mock.mock_data import MockData


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

    def test_from_dict(self):
        d = {
            AMORT.ID.value: MockData.amortFund1.amortId,
            AMORT.CCY.value: MockData.amortFund1.ccy,
            AMORT.VAL.value: MockData.amortFund1.val,
            AMORT.DATA.value: MockData.amortFund1.data
        }

        amort = Amort.fromDict(d)

        assert type(amort) is Amort

        assert amort.amortId == MockData.amortFund1.amortId
        assert amort.ccy == MockData.amortFund1.ccy
        assert amort.data == MockData.amortFund1.data
        assert amort.val == MockData.amortFund1.val
