from src.init import Init

if __name__ == '__main__':
    ctrl = Init()()

    # kold = '350151'
    # desembsInFund = ctrl.getDesembsInFundByKold(kold)
    # for desemb in desembsInFund:
    #     print(desemb)
    # print()
    # fund = ctrl.getFundByKold(kold)
    # print(fund)

    # amorts = ctrl.getAmortFundsByFundId(2)
    # [print(amort) for amort in amorts]

    # remain = ctrl.getRemainPrincInFundById(4)
    # print(remain)

    amorts = ctrl.getAmortDesembsByDesembId(1)
    [print(amort) for amort in amorts]

    pass
