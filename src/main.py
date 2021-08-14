from src.init import Init

if __name__ == '__main__':
    ctrl = Init()()

    kold = '350151'
    desembsInFund = ctrl.getDesembsInFundByKold(kold)
    for desemb in desembsInFund:
        print(desemb)
    print()
    fund = ctrl.getFundByKold(kold)
    print(fund)

    pass
