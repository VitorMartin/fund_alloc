from enum import Enum


class STATUS_CODE(Enum):
    def __str__(self):
        return self.value

    OK = 200
