#获取配置文件路径
import os
from utils.YamlUtil import YamlReader

#获取项目的基本目录
#获取当前项目的绝对路径
current = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(current))
#定义config目录的路径
_config_path=BASE_DIR + os.sep + "config"
#定义conf.yml文件的路径
_config_file=_config_path + os.sep + "conf.yml"
#定义logs文件路径
_log_path=BASE_DIR + os.sep + "logs"
#定义db_conf.yml路径
_db_config_file=_config_path + os.sep + "db_conf.yml"
#定义data目录的路径
_data_path = BASE_DIR + os.sep + "data"
#定义report目录的路径
_report_path = BASE_DIR + os.sep + "report"

#因为config与conf.yml定义的是私有变量，创建方法去返回
def get_config_path():
    return _config_path

def get_config_fiel():
    return _config_file

def get_log_path():
    return _log_path

def get_db_config_file():
    return _db_config_file

def get_data_path():
    return _data_path

def get_report_path():
    return _report_path

#读取配置文件
class ConfigYaml:
    def __init__(self):
        self.config=YamlReader(get_config_fiel()).data()
        self.db_config = YamlReader(get_db_config_file()).data()
    #获取URL
    def get_conf_url(self):
        return self.config['BASE']['test']['url']

    #获取日志级别
    def get_conf_log(self):
        return self.config['BASE']['log_level']

    #获取日志的扩展名
    def get_conf_log_extension(self):
        return self.config['BASE']['log_extension']

    #根据db_alias获取该名称下的数据库信息
    def get_db_conf_info(self,db_alias):
        return self.db_config[db_alias]

    #获取邮件配置相关信息
    def get_email_info(self):
        return self.config["email"]

if __name__ == '__main__':
    #print(ConfigYaml().get_conf_url())
    #print(ConfigYaml().get_conf_log())
    #print(ConfigYaml().get_conf_log_extension())
    print(ConfigYaml().get_db_conf_info("db_1"))