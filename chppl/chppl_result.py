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
        v = ChpplValidator()
        is_valid = v.is_valid(url) and v.is_header(url)
        is_blank1 = v.isInputedForm(str(data.get_name()))
        is_blank2 = v.isInputedForm(str(data.get_creator()))
        is_blank3 = v.isInputedForm(str(data.get_description()))
        is_blank = is_blank1 and is_blank2 and is_blank3
        if is_valid and is_blank:
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
