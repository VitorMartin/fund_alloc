class DealNotFound(Exception):
    def __init__(self):
        super().__init__('Deal not found.')
