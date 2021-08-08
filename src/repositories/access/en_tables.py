from enum import Enum


class TABLE(Enum):
    def __str__(self):
        return self.value

    FUNDS = 'funds'
    DESEMBS = 'desembs'
    AMORT_FUNDS = 'amort_funds'
    AMORT_DESEMBS = 'amort_desembs'
