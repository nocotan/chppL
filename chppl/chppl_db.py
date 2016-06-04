"""chppL
C/C++ package management system
created by @nocotan
"""
import os
import psycopg2
from urllib.parse import urlparse
from urllib.parse import unquote


class ChpplDB:
    def __init__(self):
        self.__LOCAL_DATABASE_URL = 'postgres://agcdhswzpdwrbp:gurQBp9jT2t1eNMHI3P7Ew5g_0@ec2-50-19-239-232.compute-1.amazonaws.com:5432/d8rjp9952jhohi'

    def connect(self):
        if not os.environ.get('DATABASE_URL'):
            os.environ['DATABASE_URL'] = self.__LOCAL_DATABASE_URL
        url = urlparse(os.environ['DATABASE_URL'])

        conn = psycopg2.connect(
                database=url.path[1:],
                user=url.username,
                password=url.password,
                host=url.hostname,
                port=url.port
        )

        return conn

    def insert_db(self, data):
        url = unquote(str(data.get_url()))
        name = str(data.get_name())
        creator = str(data.get_creator())
        description = str(data.get_description())
        q1 = "INSERT INTO libraries(url, name, creator, description) "
        q2 = "VALUES ('{}', '{}', '{}', '{}');".format(url, name, creator, description)
        return "{} {}".format(q1, q2)

    def commit_db(self, conn, cur):
        conn.commit()
        cur.close()
        conn.close()
