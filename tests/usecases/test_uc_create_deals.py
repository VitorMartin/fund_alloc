from datetime import date

import pytest

from ctrl import Ctrl
from src.models.amort_desemb import AmortDesemb
from src.models.amort_fund import AmortFund
from src.models.desemb import Desemb
from src.models.enums.ccy import CCY
from src.models.fund import Fund
from src.usecases.errors.invalid_deal_error import InvalidDealError
from src.usecases.errors.missing_amort_error import MissingAmortError
from src.usecases.errors.repeated_deal_error import RepeatedDealError

ctrl = Ctrl().ctrl


class Test_UCChangeFund:
    def test_create_fund(self):
        fundsLenBefore = len(ctrl.getAllFunds())
        amortsLenBefore = len(ctrl.getAllAmortFunds())

        fund = Fund('111', CCY.USD, 200., date(2021, 12, 10), date(2023, 12, 10))
        amorts = [
            AmortFund(fund, date(2022, 12, 10), CCY.USD, 100),
            AmortFund(fund, date(2023, 12, 10), CCY.USD, 100)
        ]
        fund = ctrl.createFund(fund, amorts)

        assert fundsLenBefore + 1 == len(ctrl.getAllFunds())
        assert amortsLenBefore + len(amorts) == len(ctrl.getAllAmortFunds())
        assert ctrl.getFundByKold(fund.kold) == fund
        assert ctrl.getFundById(fund.dealId) == fund

    def test_create_repeated_fund(self):
        fund = Fund('222', CCY.EUR, 200., date(2021, 12, 10), date(2023, 12, 10))
        amorts = [
            AmortFund(fund, date(2022, 12, 10), CCY.EUR, 100),
            AmortFund(fund, date(2023, 12, 10), CCY.EUR, 100)
        ]

        with pytest.raises(RepeatedDealError):
            ctrl.createFund(fund, amorts)
            ctrl.createFund(fund, amorts)

    def test_create_fund_without_amort(self):
        fund = Fund('333', CCY.EUR, 200., date(2021, 12, 10), date(2023, 12, 10))
        with pytest.raises(MissingAmortError):
            ctrl.createFund(fund, [])

    def test_create_desemb(self):
        desembsLenBefore = len(ctrl.getAllDesembs())
        amortsLenBefore = len(ctrl.getAllAmortDesembs())

        fund = Fund('444', CCY.USD, 500., date(2021, 12, 10), date(2023, 12, 10))
        amortsFund = [
            AmortFund(fund, date(2022, 12, 10), CCY.USD, 100),
            AmortFund(fund, date(2023, 12, 10), CCY.USD, 100)
        ]
        try:
            fund = ctrl.createFund(fund, amortsFund)
        except RepeatedDealError:
            pass
        desemb = Desemb(fund, '555', CCY.USD, 500, date(2021, 12, 10), date(2023, 12, 10))
        amortsDesemb = [
            AmortDesemb(desemb, date(2022, 12, 10), CCY.USD, 250),
            AmortDesemb(desemb, date(2023, 12, 10), CCY.USD, 250)
        ]

        desemb = ctrl.createDesemb(desemb, amortsDesemb)

        assert desembsLenBefore + 1 == len(ctrl.getAllDesembs())
        assert amortsLenBefore + len(amortsDesemb) == len(ctrl.getAllAmortDesembs())
        assert ctrl.getDesembByCcb(desemb.ccb) == desemb
        assert ctrl.getDesembById(desemb.dealId) == desemb
        assert ctrl.getFundByKold(desemb.fund.kold).toDict() == fund.toDict()
        assert ctrl.getFundById(desemb.fund.dealId).toDict() == fund.toDict()

    def test_create_desemb_without_fund(self):
        desembsLenBefore = len(ctrl.getAllDesembs())
        amortsLenBefore = len(ctrl.getAllAmortDesembs())

        desemb = Desemb(None, '666', CCY.USD, 500, date(2021, 12, 10), date(2023, 12, 10))
        amorts = [
            AmortDesemb(desemb, date(2022, 12, 10), CCY.USD, 250),
            AmortDesemb(desemb, date(2023, 12, 10), CCY.USD, 250)
        ]

        desemb = ctrl.createDesemb(desemb, amorts)

        assert desembsLenBefore + 1 == len(ctrl.getAllDesembs())
        assert amortsLenBefore + len(amorts) == len(ctrl.getAllAmortDesembs())
        assert ctrl.getDesembByCcb(desemb.ccb) == desemb
        assert ctrl.getDesembById(desemb.dealId) == desemb
        assert desemb.fund is None

    def test_create_desemb_without_amort(self):
        desembsLenBefore = len(ctrl.getAllDesembs())
        amortsLenBefore = len(ctrl.getAllAmortDesembs())

        desemb = Desemb(None, '777', CCY.USD, 500, date(2021, 12, 10), date(2023, 12, 10))

        with pytest.raises(MissingAmortError):
            ctrl.createDesemb(desemb, [])

    def test_create_desemb_invalid_fund(self):
        fund = Fund('888', CCY.USD, 500., date(2021, 12, 10), date(2023, 12, 10))
        desemb = Desemb(fund, '999', CCY.USD, 500, date(2021, 12, 10), date(2023, 12, 10))
        amortsDesemb = [
            AmortDesemb(desemb, date(2022, 12, 10), CCY.USD, 250),
            AmortDesemb(desemb, date(2023, 12, 10), CCY.USD, 250)
        ]

        with pytest.raises(InvalidDealError):
            ctrl.createDesemb(desemb, amortsDesemb)
