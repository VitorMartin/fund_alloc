from src.init import Init
from src.models.enums.config import *

if __name__ == '__main__':
    Init(_REPO_TYPE=REPO_TYPE.MOCK, _CTRL_TYPE=CTRL_TYPE.FASTAPI)()

    pass
