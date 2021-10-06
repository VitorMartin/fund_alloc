from enum import Enum


class MODEL(Enum):
    def __str__(self):
        return self.value

    DEAL = 'deal'
    FUND = 'fund'
    DESEMB = 'desemb'
    AMORT = 'amort'
    AMORT_FUND = 'amort_fund'
    AMORT_DESEMB = 'amort_desemb'


class DEAL(Enum):
    def __str__(self):
        return self.value

    ID = 'deal_id'
    CCY = 'deal_ccy'
    PRINC = 'deal_princ'
    INI = 'deal_ini'
    VENC = 'deal_venc'


class FUND(Enum):
    def __str__(self):
        return self.value

    ID = 'fund_id'
    KOLD = 'fund_kold'
    CCY = 'fund_ccy'
    PRINC = 'fund_princ'
    INI = 'fund_ini'
    VENC = 'fund_venc'


class DESEMB(Enum):
    def __str__(self):
        return self.value

    ID = 'desemb_id'
    FUND_ID = 'fund_id'
    CCB = 'desemb_ccb'
    CCY = 'desemb_ccy'
    PRINC = 'desemb_princ'
    INI = 'desemb_ini'
    VENC = 'desemb_venc'


class AMORT(Enum):
    def __str__(self):
        return self.value

    ID = 'amort_id'
    CCY = 'amort_ccy'
    VAL = 'amort_val'
    DATA = 'amort_data'


class AMORT_FUND(Enum):
    def __str__(self):
        return self.value

    ID = 'amort_fund_id'
    FUND_ID = 'fund_id'
    DATA = 'amort_fund_data'
    CCY = 'amort_fund_ccy'
    VAL = 'amort_fund_val'


class AMORT_DESEMB(Enum):
    def __str__(self):
        return self.value

    ID = 'amort_desemb_id'
    DESEMB_ID = 'desemb_id'
    DATA = 'amort_desemb_data'
    CCY = 'amort_desemb_ccy'
    VAL = 'amort_desemb_val'


class FLOW_CHANGE(Enum):
    def __str__(self):
        return self.value

    OP = 'op_obj'
    TYPE = 'op_type'
    DATA = 'op_data'
    VAL = 'op_val'
    FUND_PRINC = 'fund_princ'
    DESEMB_PRINC = 'desemb_princ'
    AVAIL_BEFORE = 'avail_before'
    AVAIL_AFTER = 'avail_after'

