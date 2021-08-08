from enum import Enum


class CONFIG(Enum):
    CONFIG_PATH = './src/config.json'

    REPOSITORY_TYPE = 'repository_type'
    CONTROLLER_TYPE = 'controller_type'

    MOCK = 'mock'
    ACCESS = 'access'

    FUNC = 'func'

    def __str__(self):
        return self.value
