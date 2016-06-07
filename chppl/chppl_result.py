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
        is_valid = v.is_valid_url(url) and v.is_header(url)
        is_escape1 = v.validate_injection(url)
        is_escape2 = v.validate_injection(data.get_creator())
        is_escape3 = v.validate_injection(data.get_name())
        is_escape4 = v.validate_injection(data.get_description())
        is_escape = is_escape1 and is_escape2 and is_escape3 and is_escape4
        is_blank1 = v.is_inputedForm(str(data.get_name()))
        is_blank2 = v.is_inputedForm(str(data.get_creator()))
        is_blank3 = v.is_inputedForm(str(data.get_description()))
        is_blank = is_blank1 and is_blank2 and is_blank3
        print(is_blank)
        print(is_valid)
        if is_valid and is_blank and is_escape:
            return "Success"
        else:
            return "Failed"

    def confilm_data(self):
        """data confilm
        @return: Success or Failed
        """
        data = self.__data
        package = data.get_package()
        confilm = data.get_confilm()

        v = ChpplValidator()
        is_escape1 = v.validate_injection(package)
        is_escape2 = v.validate_injection(confilm)
        is_escape = is_escape1 and is_escape2

        if package == confilm and is_escape:
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

    def delete_data(self):
        """execute delete query"""
        data = self.__data
        db = ChpplDB()
        query = db.delete_data(data)

        conn = db.connect()
        cur = conn.cursor()
        cur.execute(query)
        db.commit_db(conn, cur)
