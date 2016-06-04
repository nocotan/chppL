"""chppl.
C/C++ package management system.
created by @nocotan
"""


class ChpplData:
    def __init__(self):
        self.__url = ""
        self.__description = ""

    def get_url(self):
        return self.__url

    def set_url(self, url):
        self.__url = url

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description
