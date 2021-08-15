from enum import Enum


class CONFIG(Enum):
    def __str__(self):
        return self.value

    CONFIG_PATH = './config.json'

    REPOSITORY_TYPE = 'repository_type'
    CONTROLLER_TYPE = 'controller_type'


class REPO_TYPE(Enum):
    def __str__(self):
        return self.value

    MOCK = 'mock'
    ACCESS = 'access'


class CTRL_TYPE(Enum):
    def __str__(self):
        return self.value

    FUNC = 'func'
    FASTAPI = 'fastapi'
