import requests
from utils.LogUtil import my_log

#get方法封装
def requests_get(url,headers=None,json=None):
    response = requests.get(url,headers=headers,json=json)
    code = response.status_code
    try:
        body = response.json()
    except Exception as e:
        body = response.text
    res_dict = dict()
    res_dict['code'] = code
    res_dict['body'] = body
    return res_dict

#post方法封装
def requests_post(url,headers=None,json=None):
    response = requests.post(url=url,headers=headers,json=json)
    code = response.status_code
    try:
        body = response.json()
    except Exception as e:
        body = response.text
    res_dict = dict()
    res_dict['code'] = code
    res_dict['body'] = body
    return res_dict

#请求重构
class Request:
    def __init__(self):
        self.log=my_log("Requests")
    def request_api(self,url,data=None,headers=None,json=None,cookies=None,method='get'):
        if method == 'get':
            self.log.debug("发送get请求")
            response = requests.get(url=url, data=data,headers=headers, json=json,cookies=cookies)
        elif method == 'post':
            self.log.debug("发送post请求")
            response = requests.post(url=url, data=data,headers=headers, json=json,cookies=cookies)
        code = response.status_code
        try:
            body = response.json()
        except Exception as e:
            body = response.text
        res_dict = dict()
        res_dict['code'] = code
        res_dict['body'] = body
        return res_dict

    #get请求重构
    def get(self,url,**kwargs):
        return self.request_api(url,method='get',**kwargs)

    #post请求重构
    def post(self,url,**kwargs):
        return self.request_api(url, method='post', **kwargs)