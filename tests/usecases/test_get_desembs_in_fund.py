from typing import List

from ctrl import Ctrl
from src.models.desemb import Desemb
from src.repositories.mock.mock_data import MockData

ctrl = Ctrl().ctrl


class Test_UCGetDesembsInFund:
    def test_get_desembs_in_fund_by_kold(self):
        actualDesembs = sorted(ctrl.getDesembsInFundByKold('350151'), key=lambda desemb: desemb.venc)
        expectedDesembs = [MockData.desemb4, MockData.desemb2, MockData.desemb3]

        assert isinstance(actualDesembs, List)
        assert [isinstance(desemb, Desemb) for desemb in actualDesembs]
        assert actualDesembs == expectedDesembs
