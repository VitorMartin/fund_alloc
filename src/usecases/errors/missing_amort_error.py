class MissingAmortError(Exception):
    def __init__(self):
        super().__init__('Missing amort for this deal.')
