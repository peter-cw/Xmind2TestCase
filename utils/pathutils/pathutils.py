from os import path
import os
class PathUtils(object):

    def check_path_exists(self,path:str):
        return path.exists(path)

    def check_file_type(self,path,filename_suffix:str):
        p1,p2 = os.path.splitext(path)
        if filename_suffix in p2:
            return True
        return False

    def mk_dirs(self,path):
        '''

        :param path: an absolute path string of a directory or a file
        :return:
        '''
        dirs = path
        if os.path.isfile(path):
            dirs,file = os.path.split(path)

        os.makedirs(dirs)

    # def get_current_path(self,path):
    #     os.path.abspath(__file__)