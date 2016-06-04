"""chppL
C/C++ package management system
created by @nocotan
"""
from chppl_data import ChpplData
from chppl_validator import ChpplValidator
from chppl_db import ChpplDB


class ChpplResult(ChpplData):
    def __init__(self):
        self.__data = ChpplData()

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    def check_data(self):
        data = self.__data
        url = str(data.get_url())
        validator = ChpplValidator()
        if validator.isExitURL(url) and validator.isGithubURL(url):
            return "Success"
        else:
            return "Failed"

    def execute_query(self):
        data = self.__data
        db = ChpplDB()
        query = db.insert_db(data)

        conn = db.connect()
        cur = conn.cursor()

        cur.execute(query)
