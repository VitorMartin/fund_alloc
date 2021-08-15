from enum import Enum


class CONFIG(Enum):
    def __str__(self):
        return self.value

    CONFIG_PATH = './config.json'

    REPOSITORY_TYPE = 'repository_type'
    CONTROLLER_TYPE = 'controller_type'

    MOCK = 'mock'
    ACCESS = 'access'

    FUNC = 'func'
