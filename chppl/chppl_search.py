"""chppL
C/C++ package management system
created by @nocotan
"""
from chppl_db import ChpplDB


class ChpplSearch:
    def __init__(self):
        self.__search_list = []

    def search_all(self):
        db = ChpplDB()
        conn = db.connect()
        cur = conn.cursor()
        query = db.select_all()
        cur.execute(query)

        result = cur.fetchall()
        for row in result:
            self.__search_list.append(row)

        cur.close()
        conn.close()

    def get_search_list(self):
        return self.__search_list
