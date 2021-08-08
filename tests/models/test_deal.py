from datetime import date

from src.models.deal import Deal
from src.models.enums.ccy import CCY
from src.models.enums.dict_keys import *
from src.repositories.mock.mock_data import MockData


class Test_Deal:
    def test_instance(self):
        pk = 1
        ccy = CCY.USD
        princ = 500.66
        ini = date(2020, 1, 30)
        venc = date(2020, 12, 30)

        deal = Deal(ccy, princ, ini, venc, pk=pk)

        assert type(deal) is Deal

        assert deal.dealId == pk
        assert deal.ccy == ccy
        assert deal.princ == princ
        assert deal.ini == ini
        assert deal.venc == venc

    def test_from_dict(self):
        d = {
            DEAL.ID.value: MockData.fund1.dealId,
            DEAL.CCY.value: MockData.fund1.ccy,
            DEAL.PRINC.value: MockData.fund1.princ,
            DEAL.INI.value: MockData.fund1.ini,
            DEAL.VENC.value: MockData.fund1.venc
        }

        deal = Deal.fromDict(d)

        assert type(deal) is Deal

        assert deal.dealId == MockData.fund1.dealId
        assert deal.ccy == MockData.fund1.ccy
        assert deal.princ == MockData.fund1.princ
        assert deal.ini == MockData.fund1.ini
        assert deal.venc == MockData.fund1.venc
