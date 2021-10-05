class RepositoryError(Exception):
    def __init__(self):
        super().__init__('Repository error.')
