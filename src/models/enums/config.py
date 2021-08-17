from enum import Enum


class CONFIG(Enum):
    def __str__(self):
        return self.value

    CONFIG_FILENAME = 'config.json'

    DEPLOYMENT_TYPE = 'deployment_type'
    REPOSITORY_TYPE = 'repository_type'
    CONTROLLER_TYPE = 'controller_type'


class DEPLOYMENT_TYPE(Enum):
    def __str__(self):
        return self.value

    DEV = 'dev'
    PROD = 'prod'


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
