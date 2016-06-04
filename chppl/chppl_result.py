"""chppL
C/C++ package management system
created by @nocotan
"""
from chppl_data import ChpplData


class ChpplResult(ChpplData):
    def __init__(self):
        self.__data

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data
