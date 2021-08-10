from datetime import date

from src.models.deal import Deal
from src.models.enums.ccy import CCY
from src.models.enums.dict_keys import *
from src.repositories.mock.mock_data import MockData


class Test_Deal:
    def test_instance(self):
        deal = Deal(
            MockData.deal1.ccy,
            MockData.deal1.princ,
            MockData.deal1.ini,
            MockData.deal1.venc,
            MockData.deal1.dealId
        )

        assert isinstance(deal, Deal)
        assert deal == MockData.deal1

    def test_from_dict(self):
        d = {
            DEAL.ID.value: MockData.deal1.dealId,
            DEAL.CCY.value: MockData.deal1.ccy,
            DEAL.PRINC.value: MockData.deal1.princ,
            DEAL.INI.value: MockData.deal1.ini,
            DEAL.VENC.value: MockData.deal1.venc
        }

        deal = Deal.fromDict(d)

        assert isinstance(deal, Deal)
        assert deal == MockData.deal1
