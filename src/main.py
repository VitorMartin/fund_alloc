from prettytable.prettytable import PrettyTable

from src.init import Init
from src.models.enums.dict_keys import *
from src.repositories.mock.mock_data import MockData

if __name__ == '__main__':
    ctrl = Init()()

    # Example of searching for a new fund
    desemb = MockData.desemb2
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
    print()
    flow = ctrl.generateAmortsInFundByKold(fund.kold)
    printTable = PrettyTable(['Count', 'Type', 'Date', 'Value'], title='Amorts in original fund')
    for i in range(len(flow)):
        movement = flow[i]
        type = movement.__class__.__name__
        date = movement.data
        value = movement.val
        printTable.add_row([i+1, type, date, value])
    print(printTable)
    print()
    printTable = PrettyTable(
        ['Count', 'Type', 'Data', 'Val', 'Fund Princ', 'Desemb Princ', 'Avail Before', 'Avail After'],
        title='Complete cash flow fund'
    )
    fundAvail = ctrl.generateFundAvailByKold(fund.kold)
    for i in range(len(fundAvail)):
        movement = fundAvail[i]
        printTable.add_row([
            i + 1,
            movement[MOVEMENT.TYPE.value],
            movement[MOVEMENT.DATA.value],
            movement[MOVEMENT.VAL.value],
            movement[MOVEMENT.FUND_PRINC.value],
            movement[MOVEMENT.DESEMB_PRINC.value],
            movement[MOVEMENT.AVAIL_BEFORE.value],
            movement[MOVEMENT.AVAIL_AFTER.value]
        ])
    print(printTable)

    pass
