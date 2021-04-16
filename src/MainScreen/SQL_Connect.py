import pyodbc
import json
from os import getcwd
from collections import namedtuple

class Connector():
    def __init__(self):
        with open("config.json", 'r') as jsonLoad:
            self.jsonData   = json.load(jsonLoad)
        jsonLoad.close()

        self.cnxn   = pyodbc.connect(
            'Driver={SQL Server};'
            'Server=%s;'
            'Database=%s;'
            'UID=%s;'
            'PWD=%s;' % (
                self.jsonData['Connector']['Server'],
                self.jsonData['Connector']['Database'],
                self.jsonData['Connector']['User'],
                self.jsonData['Connector']['Password']
            )
        )

        self.cursor = self.cnxn.cursor()

    def return_all_users(self):
        data_tuple  = namedtuple('Data', 'ID User Name')
        self.cursor.execute('SELECT USERNAME as "USER", ID AS "ID", FIRSTNAME AS "NAME" FROM USERS')
        array   = []
        for row in self.cursor:
            s   = data_tuple(row.ID, row.USER, row.NAME)
            array.append(s)

        return array