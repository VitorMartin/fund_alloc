from enum import Enum


class CCY(Enum):
    def __str__(self):
        return self.value

    USD = 'USD'
    EUR = 'EUR'
