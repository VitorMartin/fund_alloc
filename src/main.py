import uvicorn

from src.init import Init
from src.models.enums.config import *

if __name__ == '__main__':
    init = Init(_REPO_TYPE=REPO_TYPE.MOCK, _CTRL_TYPE=CTRL_TYPE.FASTAPI)()
    repo = init[CONFIG.REPOSITORY_TYPE.value]
    ctrl = init[CONFIG.CONTROLLER_TYPE.value]
    adapters = init[CONFIG.ADAPTERS.value]


    uvicorn.run(ctrl.app, host=ctrl.host, port=ctrl.port)

    pass
