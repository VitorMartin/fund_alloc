from enum import Enum


class TABLES(Enum):
    def __str__(self):
        return self.value

    FUNDS = 'funds'
    DESEMBS = 'desembs'
    AMORT_FUNDS = 'amort_funds'
    AMORT_DESEMBS = 'amort_desembs'


class FUNDS(Enum):
    def __str__(self):
        return self.value

    ID = 'id'
    KOLD = 'kold'
    CCY = 'ccy'
    PRINC = 'princ'
    INI = 'ini'
    VENC = 'venc'


class DESEMBS(Enum):
    def __str__(self):
        return self.value

    ID = 'id'
    FUND = 'fund'
    CCB = 'ccb'
    CCY = 'ccy'
    PRINC = 'princ'
    INI = 'ini'
    VENC = 'venc'


class AMORT_FUNDS(Enum):
    def __str__(self):
        return self.value

    ID = 'id'
    FUND = 'fund'
    DATA = 'data'
    CCY = 'ccy'
    VAL = 'val'


class AMORT_DESEMBS(Enum):
    def __str__(self):
        return self.value

    ID = 'id'
    DESEMB = 'desemb'
    DATA = 'data'
    CCY = 'ccy'
    VAL = 'val'
