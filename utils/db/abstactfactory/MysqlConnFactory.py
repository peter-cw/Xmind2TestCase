from .AbsDbFactory import AbsractDbConnFactory
import pymysql
from dbutils.pooled_db import  PooledDB
import threading
class MysqlConnFactory(AbsractDbConnFactory):
    #数据库连接池对象
    __pool = None
    #数据库连接对象
    __conn = None

    __thread_lock = threading.Lock()

    def __init__(self,*args,**kwargs):
        self.args=args
        self.kwargs = kwargs

    def get_conn_single(self):
        if self.__conn is None:
            with self.__thread_lock:
                if self.__conn is None:
                    self.__conn = pymysql.Connect(*self.args,**self.kwargs)
        return self.__conn

    def get_conn_pool(self):
        if self.__pool is None:
            with self.__thread_lock:
                if self.__pool is None:
                    self.__pool = PooledDB(*self.args,**self.kwargs)
        return self.__pool.connection()

    def close_conn(self):
        self.__conn.close()

    def close_pool(self):
        self.__pool.close()

