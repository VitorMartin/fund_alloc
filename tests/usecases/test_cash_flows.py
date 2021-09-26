from ctrl import Ctrl

from src.models.amort import Amort
from src.models.enums.dict_keys import *
from src.repositories.mock.mock_data import MockData

ctrl = Ctrl().ctrl


class Test_UCgetValues:
    def test_generate_fund_flow_by_kold(self):
        fund = MockData.fund2
        actualFlow = ctrl.generateFundFlowByKold(fund.kold)
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

    def test_generate_fund_avail_by_kold(self):
        actualFlow = ctrl.generateFundAvailabilityByKold(MockData.fund1.kold)

        expectedFlow = [
            {
                MOVEMENT.OP.value: MockData.desemb1,
                MOVEMENT.TYPE.value: MODEL.DESEMB.value,
                MOVEMENT.DATA.value: MockData.desemb1.ini,
                MOVEMENT.VAL.value: MockData.desemb1.princ,
                MOVEMENT.FUND_PRINC.value: 0.,
                MOVEMENT.DESEMB_PRINC.value: MockData.desemb1.princ,
                MOVEMENT.AVAIL_BEFORE.value: 0.,
                MOVEMENT.AVAIL_AFTER.value: -MockData.desemb1.princ
            },
            {
                MOVEMENT.OP.value: MockData.fund1,
                MOVEMENT.TYPE.value: MODEL.FUND.value,
                MOVEMENT.DATA.value: MockData.fund1.ini,
                MOVEMENT.VAL.value: MockData.fund1.princ,
                MOVEMENT.FUND_PRINC.value: MockData.fund1.princ,
                MOVEMENT.DESEMB_PRINC.value: MockData.desemb1.princ,
                MOVEMENT.AVAIL_BEFORE.value: -MockData.desemb1.princ,
                MOVEMENT.AVAIL_AFTER.value: -MockData.desemb1.princ + MockData.fund1.princ
             },
            {
                MOVEMENT.OP.value: MockData.amortFund1,
                MOVEMENT.TYPE.value: MODEL.AMORT_FUND.value,
                MOVEMENT.DATA.value: MockData.amortFund1.data,
                MOVEMENT.VAL.value: MockData.amortFund1.val,
                MOVEMENT.FUND_PRINC.value: MockData.fund1.princ,
                MOVEMENT.DESEMB_PRINC.value: MockData.desemb1.princ,
                MOVEMENT.AVAIL_BEFORE.value: 500_000.,
                MOVEMENT.AVAIL_AFTER.value: -MockData.amortFund1.val + 500_000.
            },
            {
                MOVEMENT.OP.value: MockData.amortDesemb1,
                MOVEMENT.TYPE.value: MODEL.AMORT_DESEMB.value,
                MOVEMENT.DATA.value: MockData.amortDesemb1.data,
                MOVEMENT.VAL.value: MockData.amortDesemb1.val,
                MOVEMENT.FUND_PRINC.value: MockData.fund1.princ,
                MOVEMENT.DESEMB_PRINC.value: MockData.desemb1.princ,
                MOVEMENT.AVAIL_BEFORE.value: -1_500_000.,
                MOVEMENT.AVAIL_AFTER.value: MockData.amortDesemb1.val - 1_500_000.
            },
            {
                MOVEMENT.OP.value: MockData.amortFund2,
                MOVEMENT.TYPE.value: MODEL.AMORT_FUND.value,
                MOVEMENT.DATA.value: MockData.amortFund2.data,
                MOVEMENT.VAL.value: MockData.amortFund2.val,
                MOVEMENT.FUND_PRINC.value: MockData.fund1.princ,
                MOVEMENT.DESEMB_PRINC.value: MockData.desemb1.princ,
                MOVEMENT.AVAIL_BEFORE.value: 250_000.,
                MOVEMENT.AVAIL_AFTER.value: -MockData.amortFund2.val + 250_000.
            },
            {
                MOVEMENT.OP.value: MockData.amortDesemb2,
                MOVEMENT.TYPE.value: MODEL.AMORT_DESEMB.value,
                MOVEMENT.DATA.value: MockData.amortDesemb2.data,
                MOVEMENT.VAL.value: MockData.amortDesemb2.val,
                MOVEMENT.FUND_PRINC.value: MockData.fund1.princ,
                MOVEMENT.DESEMB_PRINC.value: MockData.desemb1.princ,
                MOVEMENT.AVAIL_BEFORE.value: -1_750_000.,
                MOVEMENT.AVAIL_AFTER.value: MockData.amortDesemb2.val - 1_750_000.
            }
        ]
        expectedFlow.sort(key=lambda movement: movement[MOVEMENT.DATA.value])

        assert len(actualFlow) == len(expectedFlow)

        for i in range(len(actualFlow)):
            actualMovement = actualFlow[i]
            actualMovement[MOVEMENT.OP.value] = actualMovement[MOVEMENT.OP.value].__str__()
            expectedMovement = expectedFlow[i]
            expectedMovement[MOVEMENT.OP.value] = expectedMovement[MOVEMENT.OP.value].__str__()

            assert isinstance(actualMovement, dict)
            assert actualMovement == expectedMovement
