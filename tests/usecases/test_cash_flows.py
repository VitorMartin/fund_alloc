import pytest
from fastapi import HTTPException

from ctrl import Ctrl

from src.models.amort import Amort
from src.models.enums.dict_keys import *
from src.repositories.mock.mock_data import MockData

ctrl = Ctrl().ctrl


class Test_UCgetValues:
    def test_get_amorts_in_fund_by_kold(self):
        fund = MockData.fund2
        actualFlow = ctrl.getAmortsInFundByKold(fund.kold)
        expectedFlow = [
            MockData.amortFund3,
            MockData.amortFund4,
            MockData.amortFund5,
            MockData.amortFund6,
            MockData.amortFund7,
            MockData.amortDesemb3,
            MockData.amortDesemb4,
            MockData.amortDesemb5,
            MockData.amortDesemb6,
            MockData.amortDesemb7,
            MockData.amortDesemb8,
            MockData.amortDesemb9,
            MockData.amortDesemb10,
            MockData.amortDesemb11,
            MockData.amortDesemb12,
        ]
        expectedFlow.sort(key=lambda amort: amort.data)

        assert len(actualFlow) == len(expectedFlow)

        for i in range(len(actualFlow)):
            actualMovement = actualFlow[i]
            expectedMovement = expectedFlow[i]

            assert isinstance(actualMovement, Amort)
            assert actualMovement == expectedMovement

    def test_get_amorts_in_fund_not_found_by_kold(self):
        with pytest.raises(HTTPException):
            ctrl.getAmortsInFundByKold('9999')

    def test_generate_fund_avail_by_kold(self):
        actualFlow = ctrl.generateFundFlowByKold(MockData.fund1.kold)

        expectedFlow = [
            {
                FLOW_CHANGE.OP.value: MockData.desemb1,
                FLOW_CHANGE.TYPE.value: MODEL.DESEMB.value,
                FLOW_CHANGE.DATA.value: MockData.desemb1.ini,
                FLOW_CHANGE.VAL.value: MockData.desemb1.princ,
                FLOW_CHANGE.FUND_PRINC.value: 0.,
                FLOW_CHANGE.DESEMB_PRINC.value: MockData.desemb1.princ,
                FLOW_CHANGE.AVAIL_BEFORE.value: 0.,
                FLOW_CHANGE.AVAIL_AFTER.value: -MockData.desemb1.princ
            },
            {
                FLOW_CHANGE.OP.value: MockData.fund1,
                FLOW_CHANGE.TYPE.value: MODEL.FUND.value,
                FLOW_CHANGE.DATA.value: MockData.fund1.ini,
                FLOW_CHANGE.VAL.value: MockData.fund1.princ,
                FLOW_CHANGE.FUND_PRINC.value: MockData.fund1.princ,
                FLOW_CHANGE.DESEMB_PRINC.value: MockData.desemb1.princ,
                FLOW_CHANGE.AVAIL_BEFORE.value: -MockData.desemb1.princ,
                FLOW_CHANGE.AVAIL_AFTER.value: -MockData.desemb1.princ + MockData.fund1.princ
            },
            {
                FLOW_CHANGE.OP.value: MockData.amortFund1,
                FLOW_CHANGE.TYPE.value: MODEL.AMORT_FUND.value,
                FLOW_CHANGE.DATA.value: MockData.amortFund1.data,
                FLOW_CHANGE.VAL.value: MockData.amortFund1.val,
                FLOW_CHANGE.FUND_PRINC.value: MockData.fund1.princ,
                FLOW_CHANGE.DESEMB_PRINC.value: MockData.desemb1.princ,
                FLOW_CHANGE.AVAIL_BEFORE.value: 500_000.,
                FLOW_CHANGE.AVAIL_AFTER.value: -MockData.amortFund1.val + 500_000.
            },
            {
                FLOW_CHANGE.OP.value: MockData.amortDesemb1,
                FLOW_CHANGE.TYPE.value: MODEL.AMORT_DESEMB.value,
                FLOW_CHANGE.DATA.value: MockData.amortDesemb1.data,
                FLOW_CHANGE.VAL.value: MockData.amortDesemb1.val,
                FLOW_CHANGE.FUND_PRINC.value: MockData.fund1.princ,
                FLOW_CHANGE.DESEMB_PRINC.value: MockData.desemb1.princ,
                FLOW_CHANGE.AVAIL_BEFORE.value: -1_500_000.,
                FLOW_CHANGE.AVAIL_AFTER.value: MockData.amortDesemb1.val - 1_500_000.
            },
            {
                FLOW_CHANGE.OP.value: MockData.amortFund2,
                FLOW_CHANGE.TYPE.value: MODEL.AMORT_FUND.value,
                FLOW_CHANGE.DATA.value: MockData.amortFund2.data,
                FLOW_CHANGE.VAL.value: MockData.amortFund2.val,
                FLOW_CHANGE.FUND_PRINC.value: MockData.fund1.princ,
                FLOW_CHANGE.DESEMB_PRINC.value: MockData.desemb1.princ,
                FLOW_CHANGE.AVAIL_BEFORE.value: 250_000.,
                FLOW_CHANGE.AVAIL_AFTER.value: -MockData.amortFund2.val + 250_000.
            },
            {
                FLOW_CHANGE.OP.value: MockData.amortDesemb2,
                FLOW_CHANGE.TYPE.value: MODEL.AMORT_DESEMB.value,
                FLOW_CHANGE.DATA.value: MockData.amortDesemb2.data,
                FLOW_CHANGE.VAL.value: MockData.amortDesemb2.val,
                FLOW_CHANGE.FUND_PRINC.value: MockData.fund1.princ,
                FLOW_CHANGE.DESEMB_PRINC.value: MockData.desemb1.princ,
                FLOW_CHANGE.AVAIL_BEFORE.value: -1_750_000.,
                FLOW_CHANGE.AVAIL_AFTER.value: MockData.amortDesemb2.val - 1_750_000.
            }
        ]
        expectedFlow.sort(key=lambda movement: movement[FLOW_CHANGE.DATA.value])

        assert len(actualFlow) == len(expectedFlow)

        for i in range(len(actualFlow)):
            actualMovement = actualFlow[i]
            actualMovement[FLOW_CHANGE.OP.value] = actualMovement[FLOW_CHANGE.OP.value].__str__()
            expectedMovement = expectedFlow[i]
            expectedMovement[FLOW_CHANGE.OP.value] = expectedMovement[FLOW_CHANGE.OP.value].__str__()

            assert isinstance(actualMovement, dict)
            assert actualMovement == expectedMovement

    def test_generate_fund_avail_not_found_by_kold(self):
        with pytest.raises(HTTPException):
            ctrl.generateFundFlowByKold('9999')
