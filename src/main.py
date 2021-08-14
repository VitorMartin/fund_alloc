from src.init import Init

if __name__ == '__main__':
    ctrl = Init()()

    kold = '350151'
    fundId = 2
    desembId = 2

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
    for desemb in desembsInFund:
        print(desemb)

    print()

    print('Get Amort Desembs by Desemb ID')
    amorts = ctrl.getAmortDesembsByDesembId(desembId)
    [print(amort) for amort in amorts]

    print()

    print('Get remaining principal in Fund by ID')
    remainFund = ctrl.getRemainPrincInFundById(fundId)
    print(remainFund)

    print()

    print('Get remaining principal in Desemb by ID')
    remainDesemb = ctrl.getRemainPrincInDesembById(desembId)
    print(remainDesemb)

    pass
