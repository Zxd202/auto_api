from utils.LogUtil import my_log
import json

class AssertUtil:
    def __init__(self):
        self.log = my_log("AssertUtil")
    #验证码相等
    def assert_code(self,code,expected_code):
        try:
            assert int(code) == int(expected_code)
            return True
        except:
            self.log.error("code error,code is %s,expected_code is %s"%(code,expected_code))
            raise
    #body相等
    def assert_body(self,body,expected_body):
        try:
            assert body == expected_body
            return True
        except:
            self.log.error("body error,body is %s,expected_body is %s"%(body,expected_body))
            raise
    #body包含期望的body
    def assert_in_body(self,body,expected_body):
        try:
            body = json.dumps(body)
            assert expected_body in body
            return True
        except:
            self.log.error("不包含或者body是错误，body is %s,expected_body is %s"%(body,expected_body))
            raise