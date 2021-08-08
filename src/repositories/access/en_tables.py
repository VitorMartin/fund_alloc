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

    ID = 'fund_id'
    KOLD = 'fund_kold'
    CCY = 'fund_ccy'
    PRINC = 'fund_princ'
    INI = 'fund_ini'
    VENC = 'fund_venc'


class DESEMBS(Enum):
    def __str__(self):
        return self.value

    ID = 'desemb_id'
    FUND_ID = 'fund_id'
    CCB = 'desemb_ccb'
    CCY = 'desemb_ccy'
    PRINC = 'desemb_princ'
    INI = 'desemb_ini'
    VENC = 'desemb_venc'


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
