"""chppL
C/C++ package management system
created by @nocotan
"""
import urllib2
from urlparse import urlparse


class ChpplValidator:
    def __init__(self):
        self.__URL_IS_NOT_VALID = "URL is not valid."

    def __del__(self):
        pass

    def isExitURL(self, url):
        try:
            f = urllib2.urlopen(url)
            f.close()
        except urllib2.HTTPError:
            return self.__URL_IS_NOT_VALID

    def isGithubURL(self, url):
        result = urlparse(url).netloc
        if str(result) == 'github.com' or str(result) == 'www.github.com':
            return True
        else:
            return False

if __name__ == '__main__':
    c = ChpplValidator()
    print c.isGithubURL("https://github.com/nocotan")
    print c.isGithubURL("https://sss.com")
