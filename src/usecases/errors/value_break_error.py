class ValueBreakError(Exception):
    def __init__(self):
        super().__init__('Too much principal allocated into this fund.')
