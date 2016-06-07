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

    def is_valid_url(self, url):
        """check url is valid or not
        @return: True or False
        """
        r1 = urlparse(unquote(str(url))).scheme
        r2 = urlparse(unquote(str(url))).netloc
        is_exit = str(r1) == 'http' or str(r1) == 'https'
        is_git = str(r2) == 'github.com' or str(r2) == 'www.github.com'
        if is_exit and is_git:
            return True
        else:
            self.__msg_list.append(self.__URL_IS_NOT_VALID)
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

    def is_inputed_form(self, param):
        """check form is blank or not.
        @return: True or False
        """
        if len(str(param)) != 0:
            return True
        else:
            self.__msg_list.append(self.__FORM_IS_BLANK)
            return False

    def validate_injection(self, param):
        """check SQL injection.
        @return: True or False
        """
        if param.find("\'") > -1 or param.find("\"") > -1:
            return False
        elif param.find("\\") > -1:
            return False
        elif param.find("<") > -1 or param.find(">") > -1:
            return False
        elif param.find("*") > -1 or param.find("=") > -1:
            return False
        elif param.find("&") > -1:
            return False
        else:
            return True

    def get_msg_list(self):
        """msg list getter."""
        return self.__msg_list
