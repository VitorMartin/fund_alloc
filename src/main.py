from src.init import Init
from src.models.enums.dict_keys import *
from src.repositories.access.en_tables import TABLE
from src.repositories.access.storage_access import StorageAccess

if __name__ == '__main__':
    ctrl = Init()()

    funds = ctrl.getAllFunds()
    for fund in funds:
        print(fund)
    print()
    desembs = ctrl.getAllDesembs()
    for desemb in desembs:
        print(desemb)
    print()
    amort_funds = ctrl.getAllAmortFunds()
    for amortFund in amort_funds:
        print(amortFund)
    print()
    amort_desembs = ctrl.getAllAmortDesembs()
    for amortDesemb in amort_desembs:
        print(amortDesemb)
    print()
    desembsInFund = ctrl.getDesembsInFundByKold('350151')
    for desemb in desembsInFund:
        print(desemb)
    print()
    db = StorageAccess()
    query = db.customQuery(f'SELECT * FROM {TABLE.FUNDS} WHERE {FUND.ID} = ? OR {FUND.ID} = ?', ['1', '2'])
    print(query)
    print()
    fundById = ctrl.getFundById(3)
    print(fundById)

    pass
