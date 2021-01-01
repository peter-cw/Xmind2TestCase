from utils.log.logutils import CustomLogger
logger = CustomLogger(__name__).get_logger()
class Test(object):
    def __enter__(self):
        print('__enter__')
        return self


    def error(self):
        raise ValueError('测试抛出错误')

    def normal(self):
        print('正常方法')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')

        if exc_type:
            print('抛出异常，exc_type为空')
            import traceback ,sys
            # traceback.print_exception(exc_type, exc_val, exc_tb, limit=2, file=sys.stdout)
            logger.error(msg=traceback.format_exc(limit=2))
        else:
            print('正常情况，不抛出异常，exc_type为空')
with Test() as t:
    t.normal()

with Test() as t:
    t.error()