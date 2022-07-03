import pymysql
from utils.LogUtil import my_log

class Mysql:
    def __init__(self,host,user,password,database,charset="utf8",port=3306):
        self.log = my_log()
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset=charset,
            port=port
        )
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
    #定义查询方法，查单条数据，多条数据
    def fetchone(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()
    def fetchall(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    #执行
    def exec(self,sql):
        try:
            if self.conn and self.cursor:
                self.cursor.execute(sql)
                self.conn.commit()
        except Exception as ex:
            self.conn.rollback()
            self.log.error("Mysql 执行失败")
            self.log.error(ex)
            return False
        return True

    #定义关闭游标，关闭数据库连接对象
    def __del__(self):
        if self.cursor is not None:
            self.cursor.close()
        if self.conn is not None:
            self.cursor.close()


if __name__ == '__main__':
    mysql = Mysql("211.103.136.242",
                  "test",
                  "test123456",
                  "meiduo",
                  charset = "utf8",
                  port=7090
                  )
    res = mysql.fetchall("select username,password from tb_users")
    print(res)
