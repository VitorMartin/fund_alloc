from datetime import date

from src.models.enums.ccy import CCY
from src.models.enums.dict_keys import *
from src.models.amort import Amort
from src.repositories.mock.mock_data import MockData


class Test_Amort:
    def test_instance(self):
        amort = Amort(
            MockData.amort1.data,
            MockData.amort1.ccy,
            MockData.amort1.val,
            pk=MockData.amort1.amortId
        )

        assert isinstance(amort, Amort)
        assert amort == MockData.amort1

    def test_from_dict(self):
        d = {
            AMORT.ID.value: MockData.amort1.amortId,
            AMORT.CCY.value: MockData.amort1.ccy,
            AMORT.VAL.value: MockData.amort1.val,
            AMORT.DATA.value: MockData.amort1.data
        }

        amort = Amort.fromDict(d)

        assert isinstance(amort, Amort)
        assert amort == MockData.amort1
