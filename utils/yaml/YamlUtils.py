import  yaml
import os
from utils.pathutils.pathutils import PathUtils
from utils.log.logutils import CustomLogger
yaml_logger = CustomLogger(name=__name__).get_logger()
class YamlUtils(object):
    @staticmethod
    def get_abs_path(path:str):
        if not os.path.isfile(path):
            yaml_logger.debug(msg='%s is an invalid argument,it must be a yaml file path string')
            return False
        dir,file = os.path.split(path)
        if not os.path.exists(dir):
            PathUtils.mk_dirs(dir)
        if PathUtils.check_file_type(file,filename_suffix='.yml'):
            return True
        return False





    @staticmethod
    def read_yaml(path):
        with open(path,mode='r',encoding='utf-8') as f:
            raw_data = f.read()
            yaml_data = yaml.full_load(f)
        return yaml_data

    @staticmethod
    def write_yaml(path,yaml_data):
        with open(path,mode='r',encoding='utf-8') as f:
            yaml.dump(yaml_data,f)

    @staticmethod
    def write_yaml_one(path,yaml_data):
        with open(path,mode='w',encoding='utf-8') as f:
            file_data = yaml.dump(yaml_data)
            f.write(file_data)

    @staticmethod
    def write_yaml_all(path,yaml_data:list):
        with open(path,mode='w',encoding='utf-8') as f:
            yaml.dump_all(yaml_data,f)

    @staticmethod
    def read_yaml_one(path):
        """
        Parse the first YAML document in a stream
        and produce the corresponding Python object.
        """
        print(path)
        with open(path,mode='r',encoding='utf-8') as f:
            # raw_data = f.read()
            # yaml_data = yaml.full_load(raw_data)
            yaml_data = yaml.full_load(f)
        print(yaml_data)
        print(type(yaml_data))
        return yaml_data


    @staticmethod
    def read_yaml_all(path):
        with open(path,mode='r',encoding='utf-8') as f:
            raw_data = f.read()
            yaml_data = yaml.full_load_all(raw_data)
        print(yaml_data)
        print(type(yaml_data))
        return list(yaml_data)



cur_path = os.path.abspath(os.path.dirname(__file__))
# c
# print(os.path.join(cur_file,'..'))
# parent_dir = os.path.abspath(cur_file)
#
# print(parent_dir)
# YamlUtils.read_yaml_one(cur_path+os.sep+'test.yml')
# data = YamlUtils.read_yaml_all(cur_path+os.sep+'test3.yml')
# print(data)
data1 = {'dev':{'host': '127.0.0.1', 'port': 8000, 'user': 'root', 'password': 'test@12345'}}
data2 = {'online':{'host': '127.0.0.1', 'port': 8000, 'user': 'root', 'password': 'test@12345'}}
# YamlUtils.read_yaml_one('test.yml')
# YamlUtils.write_yaml_one(yaml_data=data1,path=cur_path+os.sep+'test2.yml')
# YamlUtils.write_yaml_all(yaml_data=[data1,data2],path=cur_path+os.sep+'test3.yml')