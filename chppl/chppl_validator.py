"""chppL
C/C++ package management system
created by @nocotan
"""
from urllib.parse import urlparse
from urllib.parse import unquote


class ChpplValidator:
    def __init__(self):
        self.__msg_list = []
        self.__URL_IS_NOT_VALID = "URL is not valid."
        self.__URL_IS_NOT_GITHUB = "URL is not Github."
        self.__FORM_IS_BLANK = "Form is blank."

    def __del__(self):
        pass

    def isExitURL(self, url):
        result = urlparse(unquote(str(url))).scheme
        if str(result) == 'http' or str(result) == 'https':
            return True
        else:
            self.__msg_list.append(self.__URL_IS_NOT_VALID)
            return False

    def isGithubURL(self, url):
        result = urlparse(unquote(str(url))).netloc
        if str(result) == 'github.com' or str(result) == 'www.github.com':
            return True
        else:
            self.__msg_list.append(self.__URL_IS_NOT_GITHUB)
            return False

    def isInputedForm(self, param):
        if param is not "":
            return True
        else:
            self.__msg_list.append(self.__FORM_IS_BLANK)
            return False

    def get_msg_list(self):
        return self.__msg_list
