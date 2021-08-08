import enum

import pyodbc
import os

from src.interfaces.i_storage import IStorage
from src.models.desemb import Desemb
from src.repositories.access.en_tables import *


class StorageAccess(IStorage):
    __connectionStr: str
    __dbPath: str
    __connection: pyodbc.Connection
    __cursor: pyodbc.Cursor

    def __init__(self):
        self.__dbPath = os.path.join(os.path.dirname(__file__), 'db.accdb')
        self.__connectionStr = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=' + self.__dbPath
        )
        self.__connection = pyodbc.connect(self.__connectionStr)
        self.__cursor = self.__connection.cursor()

    def getAllFunds(self):
        self.__cursor.execute(f'SELECT * FROM {TABLES.FUNDS.value}')
        return self.__cursor.fetchall()

    def getAllDesembs(self):
        self.__cursor.execute(f'SELECT * FROM {TABLES.DESEMBS.value}')
        return self.__cursor.fetchall()

    def getAllAmortFunds(self):
        self.__cursor.execute(f'SELECT * FROM {TABLES.AMORT_FUNDS.value}')
        return self.__cursor.fetchall()

    def getAllAmortDesembs(self):
        self.__cursor.execute(f'SELECT * FROM {TABLES.AMORT_DESEMBS.value}')
        return self.__cursor.fetchall()

    def getDesembsInFundByKold(self, kold: str):
        self.__cursor.execute(
            f'SELECT * '
            f'FROM {TABLES.DESEMBS} INNER JOIN {TABLES.FUNDS} '
            f'ON {TABLES.FUNDS}.{FUNDS.ID} = {TABLES.DESEMBS}.{DESEMBS.FUND_ID} '
            f'WHERE {TABLES.FUNDS}.{FUNDS.KOLD} = \'{kold}\' '
            f'ORDER BY {TABLES.FUNDS}.{FUNDS.VENC}'
        )

        columns = [column[0] for column in self.__cursor.description]
        desembs = []
        for desemb in self.__cursor.fetchall():
            d = dict(zip(columns, desemb))
            desembs.append(Desemb.fromDict(d))

        return desembs
