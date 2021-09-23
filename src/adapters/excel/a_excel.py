from typing import Any, List

from src.models.desemb import Desemb
from src.models.enums.dict_keys import *
from src.models.fund import Fund


class AExcel:
    """
    Flattens all HTTP responses' dicts from CStorageFastAPI.
    """

    @staticmethod
    def flattenFunds(funds: List[Fund]) -> dict[str, Any]:
        newDict = {}
        funds = [fund.toDict() for fund in funds]

        i = 0
        numColumns = 0
        while i < len(funds):
            fund = funds[i]
            for k, v in fund.items():
                newDict[f'{k}_{i}'] = str(v)
                if i == 0:
                    numColumns += 1
            i += 1

        newDict['length'] = str(i)
        newDict['num_columns'] = str(numColumns)

        return newDict

    @staticmethod
    def flattenDesembs(desembs: List[Desemb]) -> dict[str, Any]:
        newDict = {}
        desembs = [desemb.toDict() for desemb in desembs]

        i = 0
        numColumns = 0
        while i < len(desembs):
            desemb = desembs[i]
            for kd, vd in desemb.items():
                if kd == MODEL.FUND:
                    for kf, vf in desemb[MODEL.FUND].items():
                        newDict[f'{kf}_{i}'] = vf
                        if i == 0:
                            numColumns += 1
                else:
                    newDict[f'{kd}_{i}'] = vd
                    if i == 0:
                        numColumns += 1
            i += 1

        newDict['length'] = str(i)
        newDict['num_columns'] = str(numColumns)

        return newDict
