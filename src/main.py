from src.init import Init

if __name__ == '__main__':
    ctrl = Init()()

    kold = '350151'
    fundId = 2
    desembId = 2
    desembCcb = '1159631'

    print('Get Fund by KOLD')
    fund = ctrl.getFundByKold(kold)
    print(fund)

    print()

    print('Get Amort Funds by Fund ID')
    amorts = ctrl.getAmortFundsByFundId(fundId)
    [print(amort) for amort in amorts]

    print()

    print('Get Desembs in a Fund by KOLD')
    desembsInFund = ctrl.getDesembsInFundByKold(kold)
    [print(desemb) for desemb in desembsInFund]

    print()

    print('Get Amort Desembs by Desemb ID')
    amorts = ctrl.getAmortDesembsByDesembId(desembId)
    [print(amort) for amort in amorts]

    print()

    print('Get available funds for desemb by CCB')
    availFunds = ctrl.getAvailableFundsForDesembByCcb(desembCcb)
    [print(funds) for funds in availFunds]

    pass
