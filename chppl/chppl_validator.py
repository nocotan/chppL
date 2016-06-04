"""chppL.
C/C++ package management system
created by @nocotan
"""
from urllib.parse import urlparse
from urllib.parse import unquote


class ChpplValidator:
    """form validator"""
    def __init__(self):
        """initialize
        @param: self.__msg_list
        @param: self.__URL_IS_NOT_VALID
        @param: self.__URL_IS_NOT_GITHUB
        @param: self.__FORM_IS_BLANK
        """
        self.__msg_list = []
        self.__URL_IS_NOT_VALID = "URL is not valid."
        self.__URL_IS_NOT_GITHUB = "URL is not Github."
        self.__FORM_IS_BLANK = "Form is blank."

    def isExitURL(self, url):
        """check url is exit or not
        @return: True or False
        """
        result = urlparse(unquote(str(url))).scheme
        if str(result) == 'http' or str(result) == 'https':
            return True
        else:
            self.__msg_list.append(self.__URL_IS_NOT_VALID)
            return False

    def isGithubURL(self, url):
        """check url is github or not
        @return: True or False
        """
        result = urlparse(unquote(str(url))).netloc
        if str(result) == 'github.com' or str(result) == 'www.github.com':
            return True
        else:
            self.__msg_list.append(self.__URL_IS_NOT_GITHUB)
            return False

    def is_header(self, url):
        """check url is header or not
        @return: True or False
        """
        result = urlparse(unquote(str(url))).path
        if len(str(result)) > 4:
            if str(result)[-2:] == '.h' or str(result)[-4:] == '.hpp':
                return True
            else:
                self.__msg_list.append(self.__URL_IS_NOT_VALID)
        else:
            self.__msg_list.append(self.__URL_IS_NOT_VALID)
            return False

    def isInputedForm(self, param):
        """check form is blank or not
        @return: True or False
        """
        if len(str(param)) != 0:
            return True
        else:
            self.__msg_list.append(self.__FORM_IS_BLANK)
            return False

    def get_msg_list(self):
        """msg list getter"""
        return self.__msg_list
