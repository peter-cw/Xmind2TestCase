import logging


class CustomLogger(object):
    def __init__(self,name):
        self.name = name


    def get_logger(self):
        self.logger = logging.getLogger(self.name)
        self.handler = logging.StreamHandler()
        fmt_str = 'asctime: %(asctime)s \n' \
                  'filename_line:  %(filename)s_[line:%(lineno)d] \n' \
                  'level:          %(levelname)s \n' \
                  'message:        %(message)s \n'
        formatter = logging.Formatter(fmt_str)
        self.handler.setFormatter(fmt=formatter)
        self.handler.setLevel(level=logging.DEBUG)
        self.logger.addHandler(self.handler)

        return self.logger