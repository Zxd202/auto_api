from config.Conf import ConfigYaml
from utils.MysqlUtil import Mysql
from utils.AssertUtil import AssertUtil
from utils.LogUtil import my_log
import subprocess
from utils.EmailUtil import SendEmail

log = my_log()
#初始化数据库信息
def init_db(db_alias):
    db_info = ConfigYaml().get_db_conf_info(db_alias)
    host = db_info["db_host"]
    user = db_info["db_user"]
    password = db_info["db_password"]
    db_name = db_info["db_name"]
    charset = db_info["db_charset"]
    port = int(db_info["db_port"])
    #初始化mysql对象
    conn = Mysql(host,user,password,db_name,charset,port)
    return conn

def assert_db(db_name,result,db_verify):
    assert_util = AssertUtil()
    sql = init_db(db_name)
    # 2、查询sql
    db_res = sql.fetchone(db_verify)
    # 3、数据库的结果与接口返回的结果验证
    # 打印出数据的结果
    log.debug("数据库查询结果：{}".format(str(db_res)))
    # 验证结果
    # 获取数据库结果的key,根据key获取数据库结果，接口结果
    verify_list = list(dict(db_res).keys())
    for line in verify_list:
        #res_line = response["body"][line]
        res_line = result[line]
        res_db_line = dict(db_res)[line]
        # 验证
        assert_util.assert_body(res_line, res_db_line)

#自动生成测试报告
def allure_report(report_path,report_html):
    allure_cmd = "allure generate %s -o %s --clean"%(report_path,report_html)
    log.info("报告地址")
    try:
        subprocess.call(allure_cmd,shell=True)
    except:
        log.error("用例执行失败，请检查一下测试环境相关配置")
        raise

#发送邮件
def send_mail(report_html_path="",content="",title="测试"):
    email_info = ConfigYaml().get_email_info()
    smtp_addr = email_info["smtpserver"]
    username = email_info["username"]
    password = email_info["password"]
    recv = email_info["receiver"]
    email = SendEmail(
        smtp_addr=smtp_addr,
        username=username,
        password=password,
        recv=recv,
        title=title,
        content=content,
        file=report_html_path)
    email.send_mail()

if __name__ == '__main__':
    init_db("db_1")