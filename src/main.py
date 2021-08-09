from src.init import Init
from src.repositories.access.en_tables import TABLE
from src.models.enums.dict_keys import *
from src.repositories.access.storage_access import StorageAccess

if __name__ == '__main__':
    (repo, ctrl) = Init()()

    # for fund in ctrl.getAllFunds():
    #     print(fund)
    # print()
    # for desemb in ctrl.getAllDesembs():
    #     print(desemb)
    # print()
    # for amortFund in ctrl.getAllAmortFunds():
    #     print(amortFund)
    # print()
    # for amortDesemb in ctrl.getAllAmortDesembs():
    #     print(amortDesemb)

    # for desemb in ctrl.getDesembsInFundByKold('350151'):
    #     print(desemb)

    db = StorageAccess()
    query = db.customQuery(f'SELECT * FROM {TABLE.FUNDS} WHERE {FUND.ID} = ? OR {FUND.ID} = ?', ['1', '2'])
    print(query)
