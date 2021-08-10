from datetime import date

from src.models.enums.ccy import CCY
from src.models.amort_desemb import AmortDesemb
from src.models.enums.dict_keys import *
from src.models.fund import Fund
from src.models.desemb import Desemb
from src.repositories.mock.mock_data import MockData


class Test_AmortDesemb:
    def test_instance(self):
        amortDesemb = AmortDesemb(
            Desemb(
                Fund(
                    MockData.amortDesemb1.desemb.fund.kold,
                    MockData.amortDesemb1.desemb.fund.ccy,
                    MockData.amortDesemb1.desemb.fund.princ,
                    MockData.amortDesemb1.desemb.fund.ini,
                    MockData.amortDesemb1.desemb.fund.venc,
                    pk=MockData.amortDesemb1.desemb.fund.dealId
                ),
                MockData.amortDesemb1.desemb.ccb,
                MockData.amortDesemb1.desemb.ccy,
                MockData.amortDesemb1.desemb.princ,
                MockData.amortDesemb1.desemb.ini,
                MockData.amortDesemb1.desemb.venc,
                pk=MockData.amortDesemb1.desemb.dealId
            ),
            MockData.amortDesemb1.data,
            MockData.amortDesemb1.ccy,
            MockData.amortDesemb1.val,
            pk=MockData.amortDesemb1.amortId
        )

        assert isinstance(amortDesemb, AmortDesemb)
        assert amortDesemb == MockData.amortDesemb1

    def test_from_dict(self):
        d = {
            FUND.ID.value: MockData.amortDesemb1.desemb.fund.dealId,
            FUND.KOLD.value: MockData.amortDesemb1.desemb.fund.kold,
            FUND.CCY.value: MockData.amortDesemb1.desemb.fund.ccy,
            FUND.PRINC.value: MockData.amortDesemb1.desemb.fund.princ,
            FUND.INI.value: MockData.amortDesemb1.desemb.fund.ini,
            FUND.VENC.value: MockData.amortDesemb1.desemb.fund.venc,

            DESEMB.ID.value: MockData.amortDesemb1.desemb.dealId,
            DESEMB.CCB.value: MockData.amortDesemb1.desemb.ccb,
            DESEMB.INI.value: MockData.amortDesemb1.desemb.ini,
            DESEMB.CCY.value: MockData.amortDesemb1.desemb.ccy,
            DESEMB.PRINC.value: MockData.amortDesemb1.desemb.princ,
            DESEMB.VENC.value: MockData.amortDesemb1.desemb.venc,

            AMORT_DESEMB.ID.value: MockData.amortDesemb1.amortId,
            AMORT_DESEMB.CCY.value: MockData.amortDesemb1.ccy,
            AMORT_DESEMB.VAL.value: MockData.amortDesemb1.val,
            AMORT_DESEMB.DATA.value: MockData.amortDesemb1.data
        }

        amortDesemb = AmortDesemb.fromDict(d)

        assert isinstance(amortDesemb, AmortDesemb)
        assert amortDesemb == MockData.amortDesemb1
