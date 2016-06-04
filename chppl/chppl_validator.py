"""chppL
C/C++ package management system
created by @nocotan
"""
from urlparse import urlparse


class ChpplValidator:
    def __init__(self):
        self.__msg_list = []
        self.__URL_IS_NOT_VALID = "URL is not valid."
        self.__URL_IS_NOT_GITHUB = "URL is not Github."

    def __del__(self):
        pass

    def isExitURL(self, url):
        result = urlparse(url).scheme
        if str(result) == 'http' or str(result) == 'https':
            return True
        else:
            self.__msg_list.append(self.__URL_IS_NOT_VALID)
            return False

    def isGithubURL(self, url):
        result = urlparse(url).netloc
        if str(result) == 'github.com' or str(result) == 'www.github.com':
            return True
        else:
            self.__msg_list.append(self.__URL_IS_NOT_GITHUB)
            return False

if __name__ == '__main__':
    c = ChpplValidator()
    print c.isExitURL("htts://githb.com/nocotan")
