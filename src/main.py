from src.init import Init

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

    for desemb in ctrl.getDesembsInFundByKold('350151'):
        print(desemb)
