import pymysql
import cx_Oracle
from utils.log.logutils import CustomLogger
logger = CustomLogger(__name__).get_logger()
class DatabaseAccessObject(object):
    __DB_SUPPOT_DICT = {
        'MYSQL' : 'MysqlConnFactory',
        'ORACLE' : 'cx-Oracle'
    }


    def __init__(self,db_type='mysql',use_pool=False,*args,**kwargs):
        '''

        :param db_type:数据库类型，默认为musql
        :param use_pool:是否使用连接池，默认为False
        :param args:
        :param kwargs:
        直接以可变位置参数与可变关键字参数的形式传入数据库配置参数，具体字段看不同数据库的__init__()方法
        host:str,port:str,user:str,password:str

        '''
        # self.host = host
        # self.port = port
        # self.user = user
        # self.password = password
        self.db_type = db_type
        self.use_pool = use_pool
        self.args = args
        self.kwargs = kwargs

        db_type_fmt = self.db_type.upper()
        if not db_type_fmt in self.__DB_SUPPOT_DICT.keys():
            return False
        factory_name = self.__DB_SUPPOT_DICT[db_type_fmt]
        lib = __import__('importlib')
        from .abstactfactory.MysqlConnFactory import MysqlConnFactory as factory_cls
        # factory_cls =lib.import_module(''+factory_name+'.'+factory_name)
        # factory_cls = __import__('abstractfactory.'+factory_name+'.'+factory_name)
        print(self.kwargs)
        self.factory_obj =  factory_cls(*self.args,**self.kwargs)


    def __enter__(self):

        self.get_conn()
        self.get_cursor()
        return self






    def get_conn(self):

        if self.use_pool == True:
            self.conn = self.factory_obj.get_conn_pool()
        else:
            self.conn =  self.factory_obj.get_conn_single()

    def get_cursor(self):

        self.cursor = self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        # self.factory_obj.close_conn()
        if not getattr(self.factory_obj,'__pool',None)==None:
           self.factory_obj.close_pool()


        if exc_type:
            import traceback ,sys
            traceback.print_exception(exc_type, exc_val, exc_tb, limit=2, file=sys.stdout)
            logger.error(msg=traceback.format_exc(limit=2))



    def exec_sql(self,sql:str):
        self.cursor.execute(sql)

    def excc_many(self,sql,args):
        self.cursor.executemany(sql,args)

    def fetch_one(self):
        return self.cursor.fetchone()

    def fetch_all(self):
        return self.cursor.fetchall()

    def fetch_many(self,size):
        return self.cursor.fetchmany(size)

