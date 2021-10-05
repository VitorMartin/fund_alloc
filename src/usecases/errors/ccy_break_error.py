class CcyBreakError(Exception):
    def __init__(self):
        super().__init__('Loan currency is different than fund\'s currency.')
