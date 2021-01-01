class AbsractDbConnFactory(object):

    def get_conn_single(self):
        pass

    def get_conn_pool(self):
        pass

    def close_conn(self):
        pass

    def close_pool(self):
        pass


