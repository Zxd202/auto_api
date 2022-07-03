from config import Conf
import os
from utils.YamlUtil import YamlReader
import pytest
from config.Conf import ConfigYaml
from utils.RequestsUtil import Request
from utils.AssertUtil import AssertUtil
from common import Base
import allure

#获取测试用例内容 list
test_file = os.path.join(Conf.get_data_path(),"testlogin.yml")
#使用YamlUtil工具类来读取测试用例
data_list = YamlReader(test_file).data_all()
#参数化执行用例
@pytest.mark.parametrize("login",data_list)
def test_yaml(login):
    #初始化url,data
    url = ConfigYaml().get_conf_url()+login["url"]
    data = login["data"]
    code = login["code"]
    body = login["expect_body"]
    request = Request()
    response = request.post(url,json=data)
    #断言验证
    #print(response)
    assert_util = AssertUtil()
    assert_util.assert_code(int(response["code"]),int(code))
    #assert_util.assert_in_body(str(response["body"]),str(body))
    #数据库结果断言
    db_verify = "select ..."
    Base.assert_db("db_1",response["body"],db_verify)

    #allure
    #sheet名称 feature一级标签
    allure.dynamic.feature("")
    #模块 story 二级标签
    allure.dynamic.story("")
    #用例ID+接口名称 title
    allure.dynamic.title("")
    #请求URL 请求类型 期望结果实际结果描述
    allure.dynamic.description("")

if __name__ == '__main__':
    report_path = Conf.get_report_path()+os.sep+"result"
    report_html_path = Conf.get_report_path()+os.sep+"html"
    pytest.main(["test_login.py","--alluredir",report_path])
    Base.allure_report(report_path,report_html_path)
    Base.SendEmail(title="接口测试报告结果",content=report_html_path)