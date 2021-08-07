from abc import ABC

from datetime import date

from src.models.amort_desemb import AmortDesemb
from src.models.amort_fund import AmortFund
from src.models.desemb import Desemb
from src.models.enums.ccy import CCY
from src.models.fund import Fund


class MockData(ABC):
    fund1 = Fund('350150', CCY.USD, 4_000_000,  date(2021, 12, 2), date(2023, 4, 5), pk=1)
    fund2 = Fund('350151', CCY.USD, 20_000_000, date(2020, 2, 9),  date(2025, 2, 9), pk=2)
    fund3 = Fund('984620', CCY.EUR, 1_000_000,  date(2021, 8, 25), date(2022, 1, 25), pk=3)
    fund4 = Fund('984621', CCY.EUR, 3_000_000,  date(2021, 9, 29), date(2024, 9, 29), pk=4)

    funds = [fund1, fund2, fund3, fund4]

    desemb1 = Desemb(fund1, '1159630', CCY.USD, 3_500_000,  date(2021, 10, 30), date(2023, 10, 30), pk=1)
    desemb2 = Desemb(fund2, '1159631', CCY.USD, 2_000_000,  date(2021, 9, 4),   date(2022, 9, 4), pk=2)
    desemb3 = Desemb(fund2, '1159632', CCY.USD, 10_500_000, date(2021, 12, 12), date(2024, 12, 12), pk=3)
    desemb4 = Desemb(fund2, '1159633', CCY.USD, 6_000_000,  date(2021, 11, 5),  date(2022, 5, 5), pk=4)
    desemb5 = Desemb(fund3, '1159634', CCY.EUR, 1_000_000,  date(2021, 8, 25),  date(2022, 8, 25), pk=5)
    desemb6 = Desemb(fund4, '1159635', CCY.EUR, 2_500_000,  date(2021, 10, 1),  date(2023, 10, 1), pk=6)

    desembs = [desemb1, desemb2, desemb3, desemb4, desemb5, desemb6]

    amortFund1  = AmortFund(fund1, date(2022, 4, 5),  CCY.USD, 2_000_000, pk=1)
    amortFund2  = AmortFund(fund1, date(2023, 4, 5),  CCY.USD, 2_000_000, pk=2)
    amortFund3  = AmortFund(fund2, date(2021, 2, 9),  CCY.USD, 4_000_000, pk=3)
    amortFund4  = AmortFund(fund2, date(2022, 2, 9),  CCY.USD, 2_000_000, pk=4)
    amortFund5  = AmortFund(fund2, date(2023, 2, 9),  CCY.USD, 2_000_000, pk=5)
    amortFund6  = AmortFund(fund2, date(2024, 2, 9),  CCY.USD, 2_000_000, pk=6)
    amortFund7  = AmortFund(fund2, date(2025, 2, 9),  CCY.USD, 2_000_000, pk=7)
    amortFund8  = AmortFund(fund3, date(2022, 8, 25), CCY.EUR, 1_000_000, pk=8)
    amortFund9  = AmortFund(fund4, date(2022, 9, 29), CCY.EUR, 1_000_000, pk=9)
    amortFund10 = AmortFund(fund4, date(2023, 9, 29), CCY.EUR, 1_000_000, pk=10)
    amortFund11 = AmortFund(fund4, date(2024, 9, 29), CCY.EUR, 1_000_000, pk=11)

    amortFunds = [
        amortFund1, amortFund2, amortFund3, amortFund4, amortFund5, amortFund6,
        amortFund7, amortFund8, amortFund9, amortFund10, amortFund11
    ]

    amortDesemb1  = AmortDesemb(desemb1, date(22, 10, 30),   CCY.USD, 1_750_000, pk=1)
    amortDesemb2  = AmortDesemb(desemb1, date(23, 10, 30),   CCY.USD, 1_750_000, pk=2)
    amortDesemb3  = AmortDesemb(desemb2, date(2022, 9, 4),   CCY.USD, 2_000_000, pk=3)
    amortDesemb4  = AmortDesemb(desemb3, date(2022, 12, 12), CCY.USD, 3_500_000, pk=4)
    amortDesemb5  = AmortDesemb(desemb3, date(2023, 12, 12), CCY.USD, 3_500_000, pk=5)
    amortDesemb6  = AmortDesemb(desemb3, date(2024, 12, 12), CCY.USD, 3_500_000, pk=6)
    amortDesemb7  = AmortDesemb(desemb4, date(2021, 12, 5),  CCY.USD, 1_000_000, pk=7)
    amortDesemb8  = AmortDesemb(desemb4, date(2022, 1, 5),   CCY.USD, 1_000_000, pk=8)
    amortDesemb9  = AmortDesemb(desemb4, date(2022, 2, 5),   CCY.USD, 1_000_000, pk=9)
    amortDesemb10 = AmortDesemb(desemb4, date(2022, 3, 5),   CCY.USD, 1_000_000, pk=10)
    amortDesemb11 = AmortDesemb(desemb4, date(2022, 4, 5),   CCY.USD, 1_000_000, pk=11)
    amortDesemb12 = AmortDesemb(desemb4, date(2022, 5, 5),   CCY.USD, 1_000_000, pk=12)
    amortDesemb13 = AmortDesemb(desemb5, date(2022, 8, 25),  CCY.EUR, 1_000_000, pk=13)
    amortDesemb14 = AmortDesemb(desemb6, date(2022, 10, 1),  CCY.EUR, 1_250_000, pk=14)
    amortDesemb15 = AmortDesemb(desemb6, date(2023, 10, 1),  CCY.EUR, 1_250_000, pk=15)

    amortDesembs = [
        amortDesemb1, amortDesemb2, amortDesemb3, amortDesemb4, amortDesemb5,
        amortDesemb6, amortDesemb7, amortDesemb8, amortDesemb9, amortDesemb10,
        amortDesemb11, amortDesemb12, amortDesemb13, amortDesemb14, amortDesemb15
    ]
