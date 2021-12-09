class RepositoryError(Exception):
    def __init__(self, msg=None):
        if msg:
            super().__init__(msg)
        else:
            super().__init__('Repository error.')


class NotFoundError(Exception):
    def __init__(self):
        super().__init__('Item not found.')
