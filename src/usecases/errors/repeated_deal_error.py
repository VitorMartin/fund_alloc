class RepeatedDealError(Exception):
    def __init__(self):
        super().__init__('This deal already exists.')
