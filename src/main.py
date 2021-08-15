import src.repositories.mock.mock_data
from src.init import Init

if __name__ == '__main__':
    ctrl = Init()()

    # Example of searching for a new fund
    desemb = src.repositories.mock.mock_data.MockData.desemb2
    amortDesembs = ctrl.getAmortDesembsByDesembId(desemb.dealId)
    print('Desemb:')
    print(desemb)
    print()
    print('Original fund:')
    print(desemb.fund)
    print()
    print('Available funds:')
    availFunds = sorted(ctrl.getAvailableFundsForDesembByCcb(desemb.ccb), key=lambda fund: fund.venc)
    amortFunds = []
    fundFound = False
    for fund in availFunds:
        if not fundFound:
            if fund.dealId != desemb.dealId:
                fundFound = True
                print('[FOUND] ', end='')
                selectedFund = fund
                amortFunds = ctrl.getAmortFundsByFundId(selectedFund.dealId)
        if fund.dealId == desemb.fund.dealId:
            print(' [SAME] ', end='')
        print(fund)
    print()
    print('Comparing cash flows:')
    print('\tAmort Fund:')
    [print(f'\t\t{amortFund}') for amortFund in amortFunds]
    print('\tAmort Desemb:')
    [print(f'\t\t{amortDesemb}') for amortDesemb in amortDesembs]

    pass
