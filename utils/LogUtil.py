from config import Conf
from config.Conf import ConfigYaml
import logging
import datetime,os

#定义日志级别的隐射
log_l={
    "info": logging.INFO,
    "debug": logging.DEBUG,
    "warning": logging.WARNING,
    "error": logging.ERROR
}

class Logger:
    def __init__(self,log_file,log_name,log_level):
        self.log_file=log_file
        self.log_name=log_name
        self.log_level=log_level

        #设置logger名称
        self.logger=logging.getLogger(self.log_name)
        #设置log级别
        self.logger.setLevel(log_l[self.log_level])
        #判断handlers是否存在
        if not self.logger.handlers:
            # 输出到控制台
            fh_s = logging.StreamHandler()
            fh_s.setLevel(log_l[self.log_level])
            formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
            fh_s.setFormatter(formatter)
            #写入文件
            fh_f = logging.FileHandler(self.log_file,encoding='utf-8')
            fh_f.setLevel(log_l[self.log_level])
            fh_f.setFormatter(formatter)

            #添加handler
            self.logger.addHandler(fh_s)
            self.logger.addHandler(fh_f)

#初始化参数数据
log_path=Conf.get_log_path()
current_time=datetime.datetime.now().strftime("%Y-%m-%d")
log_extension=ConfigYaml().get_conf_log_extension()
logfiel=os.path.join(log_path,current_time+log_extension)
loglevel=ConfigYaml().get_conf_log()

#对外方法
def my_log(log_name=__file__):
    return Logger(log_file=logfiel,log_name=log_name,log_level=loglevel).logger

if __name__ == '__main__':
    my_log().debug("this is debug")