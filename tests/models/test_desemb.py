from src.models.desemb import Desemb
from src.models.enums.dict_keys import *
from src.models.fund import Fund
from src.repositories.mock.mock_data import MockData


class Test_Desemb:
    def test_instance(self):
        desemb = Desemb(
            Fund(
                MockData.desemb1.fund.kold,
                MockData.desemb1.fund.ccy,
                MockData.desemb1.fund.princ,
                MockData.desemb1.fund.ini,
                MockData.desemb1.fund.venc,
                pk=MockData.desemb1.fund.dealId
            ),
            MockData.desemb1.ccb,
            MockData.desemb1.ccy,
            MockData.desemb1.princ,
            MockData.desemb1.ini,
            MockData.desemb1.venc,
            pk=MockData.desemb1.dealId
        )

        assert isinstance(desemb, Desemb)
        assert desemb == MockData.desemb1

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

        assert isinstance(desemb, Desemb)
        assert desemb == MockData.desemb1
