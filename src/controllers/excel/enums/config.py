from enum import Enum


class CONFIG(Enum):
    def __str__(self):
        return self.value

    PROTOCOL = 'protocol'
    HOST = 'host'
    PORT = 'port'


class PROTOCOL(Enum):
    def __str__(self):
        return self.value

    HTTP = 'http'
    HTTPS = 'https'


class HOST(Enum):
    def __str__(self):
        return self.value

    LOCALHOST = 'localhost'


class PORT(Enum):
    def __str__(self):
        return self.value

    DEFAULT = 80
