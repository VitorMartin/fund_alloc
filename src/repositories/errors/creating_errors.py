class UnableToCreateDealError(Exception):
    def __init__(self):
        super().__init__('Unable to create deal.')
