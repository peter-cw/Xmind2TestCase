from .AbsDbFactory import AbsractDbConnFactory
import cx_Oracle
import threading

'''
oracle尚未适配完成
'''
class OracleConnFactory(AbsractDbConnFactory):
    #数据库连接池对象
    __pool = None
    #单个数据库连接对象
    __conn = None

    __thread_lock = threading.Lock()

    def __init__(self,*args,**kwargs):
        self.args=args
        self.kwargs = kwargs

    def get_conn_single(self):
        if self.__conn is None:
            with self.__thread_lock:
                if self.__conn is None:
                    self.__conn = cx_Oracle.connect(*self.args,**self.kwargs)

        return self.__conn

    def get_conn_pool(self):
        if self.__pool is None:
            with self.__thread_lock:
                if self.__pool is None:
                    self.__pool = cx_Oracle.SessionPool(*self.args,**self.kwargs)
        self.__conn =  self.__pool.acquire()
        return self.__conn


    def clos_conn(self):
        if self.__pool:
            self.__pool.close(self.__conn)
        else:
            self.__conn.close()

    def close_pool(self):
        self.__pool.close()
