class DateBreakError(Exception):
    def __init__(self):
        super().__init__('Loan maturity longer than fund\'s maturity.')
