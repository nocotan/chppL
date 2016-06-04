"""chppL
C/C++ package management system
created by @nocotan
"""
import os
import dj_database_url
import psycopg2
import psycopg2.extras


class ChpplDB:
    def __init__(self):
        self.__local = 'postgres://test:1@localhost:54'

    def connect(self, url=None):
        if not os.environ.get('DATABASE_URL'):
            os.environ['DATABASE_URL'] = self.__local
        param = dj_database_url.config()
        return psycopg2.connect(
                dbname=param['NAME'],
                user=param['USER'],
                password=param['PASSWORD'],
                host=param['HOST'],
                port=param['PORT'],
                ).cursor(cursor_factory=psycopg2.extras.DictCursor())
