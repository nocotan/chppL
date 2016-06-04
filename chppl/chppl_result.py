"""chppL.
C/C++ package management system
created by @nocotan
"""
from chppl_data import ChpplData
from chppl_validator import ChpplValidator
from chppl_db import ChpplDB


class ChpplResult(ChpplData, ChpplValidator):
    """result of register
    inheritence:
      ChpplData,
      ChpplValidator
    """
    def __init__(self):
        """initialize
        @param: self.__data
        """
        self.__data = ChpplData()
        ChpplValidator.__init__(self)

    def set_data(self, data):
        """data setter"""
        self.__data = data

    def get_data(self):
        """data getter
        @return self.__data
        """
        return self.__data

    def check_data(self):
        """data chekker
        @return: Success or Failed
        """
        data = self.__data
        url = str(data.get_url())
        validator = ChpplValidator()
        if validator.isExitURL(url) \
                and validator.isGithubURL(url) \
                and validator.isInputedForm(str(data.get_name())) \
                and validator.isInputedForm(str(data.get_creator())) \
                and validator.isInputedForm(str(data.get_description())) \
                and validator.is_header(url):
            return "Success"
        else:
            return "Failed"

    def execute_query(self):
        """execute insert query"""
        data = self.__data
        db = ChpplDB()
        query = db.insert_db(data)

        conn = db.connect()
        cur = conn.cursor()

        cur.execute(query)

        db.commit_db(conn, cur)
