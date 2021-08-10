from src.models.enums.dict_keys import *
from src.models.fund import Fund
from src.repositories.mock.mock_data import MockData


class Test_Fund:
    def test_instance(self):
        fund = Fund(
            MockData.fund1.kold,
            MockData.fund1.ccy,
            MockData.fund1.princ,
            MockData.fund1.ini,
            MockData.fund1.venc,
            pk=MockData.fund1.dealId
        )

        assert isinstance(fund, Fund)
        assert fund == MockData.fund1

    def test_from_dict(self):
        d = {
            FUND.ID.value: MockData.fund1.dealId,
            FUND.KOLD.value: MockData.fund1.kold,
            FUND.CCY.value: MockData.fund1.ccy,
            FUND.PRINC.value: MockData.fund1.princ,
            FUND.INI.value: MockData.fund1.ini,
            FUND.VENC.value: MockData.fund1.venc
        }

        fund = Fund.fromDict(d)

        assert isinstance(fund, Fund)

        assert fund == MockData.fund1
