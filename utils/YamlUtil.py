import yaml
import os

#yaml读取封装
class YamlReader:
    def __init__(self,yamlfile):
        if os.path.exists(yamlfile):
            self.yamlfile=yamlfile
        else:
            raise FileNotFoundError('文件不存在')
        self._data=None
        self._data_all=None

    #单个文件读取
    def data(self):
        if not self._data:
            with open(self.yamlfile,'rb') as f:
                self._data=yaml.safe_load(f)
        return self._data

    #多个文件读取
    def data_all(self):
        if not self._data_all:
            with open(self.yamlfile,'rb') as f:
                self._data_all=list(yaml.safe_load_all(f))
        return self._data_all

if __name__ == '__main__':
    r=YamlReader(r'F:\API\data\testlogin.yml').data_all()
    print(r)