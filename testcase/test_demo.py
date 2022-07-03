import requests
from utils.RequestsUtil import Request
from config.Conf import ConfigYaml
import pytest
from utils.AssertUtil import AssertUtil
from common.Base import init_db

#1、登录
def test_login():
    conffiel=ConfigYaml()
    urlpath=conffiel.get_conf_url()
    url=urlpath+'/authorizations/'
    data = {
        "username":"python",
        "password":"12345678"
    }
    response = requests.post(url=url,json=data)
    return response.json()['token']

    conn = init_db("db_1")
    res_db = conn.fetchone("select id from tb_users where username='python'")
    print("数据库查询结果：%s"%res_db)
    user_id = response["user_id"]
    assert user_id == res_db["id"]
#2、个人信息
def test_info():
    conffiel = ConfigYaml()
    urlpath = conffiel.get_conf_url()
    url = urlpath + '/user/'
    token = test_login()
    headers = {
        'Authorization': 'JWT ' + token
    }
    request = Request()
    response = request.get(url=url,headers=headers)
    print(response)
    code = response["code"]
    AssertUtil().assert_code(code,200)
    body = response["body"]
    AssertUtil().assert_in_body(body,'{"id": 1, "username": "python", "mobile": "17701397029", "email": "952673638@qq.com", "email_active": true}')


#3、商品列表数据
def test_goods_list():
    conffiel = ConfigYaml()
    urlpath = conffiel.get_conf_url()
    url = urlpath + '/categories/115/skus/'
    data = {
        "page":"1",
        "page_size":"10",
        "ordering":"create_time"
    }
    request = Request()
    response = request.get(url=url,json=data)
    print(response)

#4、添加购物车
def test_cart():
    conffiel = ConfigYaml()
    urlpath = conffiel.get_conf_url()
    url = urlpath + '/cart/'
    token = test_login()
    headers = {
        'Authorization': 'JWT ' + token
    }
    data = {
        "sku_id":"3",
        "count":"1",
        "selected":"true"
    }
    request = Request()
    response = request.post(url=url,json=data,headers=headers)
    print(response)

#5、创建订单
@pytest.mark.flaky(reruns=3,reruns_delay=2)
def test_order():
    conffiel = ConfigYaml()
    urlpath = conffiel.get_conf_url()
    url = urlpath + '/cart//orders/'
    token = test_login()
    headers = {
        'Authorization': 'JWT ' + token
    }
    data = {
        "address":"1",
        "pay_method":"1"
    }
    request = Request()
    response = request.post(url=url,json=data,headers=headers)
    print(response)


if __name__ == '__main__':
    #login()
    #info()
    #goods_list()
    #cart()
    #order()
    pytest.main(['-s'])