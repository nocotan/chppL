"""chppL.
C/C++ package management system.
created by @nocotan
"""


class ChpplData:
    """main data"""
    def __init__(self):
        """initialize
        @param: __url
        @param: __name
        @param: __description
        @param: __creator
        @param: __package
        @param: __confilm
        """
        self.__url = ""
        self.__name = ""
        self.__description = ""
        self.__creator = ""
        self.__package = ""
        self.__confilm = ""

    def get_url(self):
        """url getter
        @return: self.__url
        """
        return self.__url

    def set_url(self, url):
        """url setter"""
        self.__url = url

    def get_name(self):
        """name getter
        @return: self.__name
        """
        return self.__name

    def set_name(self, name):
        """name setter"""
        self.__name = name

    def get_description(self):
        """description getter
        @return: self.__description
        """
        return self.__description

    def set_description(self, description):
        """description setter"""
        self.__description = description

    def get_creator(self):
        """creator getter
        @return: self.__creator
        """
        return self.__creator

    def set_creator(self, creator):
        """creator setter"""
        self.__creator = creator

    def get_package(self):
        """package getter
        @return: self.__package
        """
        return self.__package

    def set_package(self, package):
        """package setter"""
        self.__package = package

    def get_confilm(self):
        """confilm getter
        @return: confilm
        """
        return self.__confilm

    def set_confilm(self, confilm):
        """confilm setter"""
        self.__confilm = confilm
