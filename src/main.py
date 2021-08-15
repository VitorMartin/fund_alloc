from fastapi import FastAPI
from prettytable.prettytable import PrettyTable

from models.enums.config import *
from src.init import Init
from src.models.enums.dict_keys import *
from src.repositories.mock.mock_data import MockData

if __name__ == '__main__':
    ctrl = Init(_REPO_TYPE=REPO_TYPE.ACCESS, _CTRL_TYPE=CTRL_TYPE.FASTAPI)

    pass
