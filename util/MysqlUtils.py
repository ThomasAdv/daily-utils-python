import os
import sys
import datetime
import time

import pymysql
from pymysql.constants import CLIENT


class MysqlUtils(object):
    """ mysqldb 操作类"""
    def __init__(self, params):
        """ 数据库初始化 """
        self.host = str(params.get("host", ""))
        self.username = str(params.get("username", ""))
        self.password = str(params.get("password", ""))
        self.dbname = str(params.get("dbname", ""))
        self.port = str(params.get("port", ""))

    def connect(self):
        """ 链接数据库 """
        try:
            self.conn = pymysql.connect(host=self.host, user=self.username, passwd=self.password, db=self.dbname, port=int(self.port), charset='utf8', connect_timeout=1000, client_flag=CLIENT.MULTI_STATEMENTS)
        except Exception as e:
            print("conn mysql error: %s" % e)
        self.cursor = self.conn.cursor() # 使用cursor方法获取操作游标

    def close(self):
        """ 关闭数据库 """
        self.cursor.close()
        self.conn.close()

    def fetchall(self, sql):
        """ 用于查询返回所有结果 """
        results = []
        try:
            self.connect()
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
        except Exception as e:
            print("mysql selct  all error: %s" % e)
        return results

    def fetchone(self, sql):
        """ 查询一条结果 """
        try:
            self.connect()
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
        except Exception as e:
            self.rollback()
            print("mysql select one error: %s" % e)
        return result

    def execute(self, sql):
        """ 进行修改，插入，更新基本操作 """
        try:
            self.connect()
            self.cursor.execute(sql)
            effectRow = self.cursor.rowcount
            return effectRow
        except Exception as e:
            self.rollback()
            return ("mysql insert error: %s" % e)

    def commit(self):
        """ 事务提交操作 """
        try:
            self.conn.commit()
            return ''
        except Exception as e:
            self.rollback()
            return ("mysql commit error: %s" % e)


    def rollback(self):
        """ 事务回滚操作 """
        self.conn.rollback()

#插入 更新
def test_create_table(params):
    sql = """
    DROP TABLE IF EXISTS `time_record`;
    CREATE TABLE `time_record` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `hour` int(11) DEFAULT NULL,
      `minute` int(11) DEFAULT NULL,
      `second` int(11) DEFAULT NULL,
      `remark` varchar(100) DEFAULT NULL,
      `created_date` datetime DEFAULT NULL,
      `updated_date` datetime DEFAULT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=469 DEFAULT CHARSET=utf8;
    """
    myconn=MysqlUtils(params)
    myconn.execute(sql)
    print(myconn.commit())
    myconn.close()

def test_insert_update(params):
    sql = f"""
    INSERT INTO `time_record`(`hour`, `minute`, `second`,`remark`, `created_date`, `updated_date`) 
    VALUES ({datetime.datetime.now().hour}, {datetime.datetime.now().minute}, {datetime.datetime.now().second},
    'created', '{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', '{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'),
    ({datetime.datetime.now().hour}, {datetime.datetime.now().minute}, {datetime.datetime.now().second},
    'created', '{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', '{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
        """
    myconn=MysqlUtils(params)
    print(myconn.execute(sql))
    print(myconn.commit())

    time.sleep(2)

    update_sql = f'''
    UPDATE `time_record` SET `remark` = 'updated', `updated_date` ='{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
    '''
    print(myconn.execute(update_sql))
    print(myconn.commit())

    myconn.close()

def test_fetchone(params):
    sql = """
    select * from `time_record`
        """
    myconn=MysqlUtils(params)
    result=myconn.fetchone(sql)
    print(result,type(result))
    myconn.close()

def test_fetchall(params):
    sql = """
    select * from `time_record`
        """
    myconn=MysqlUtils(params)
    result=myconn.fetchall(sql)
    print(result,type(result))
    myconn.close()


if __name__ == '__main__':
    params = {"host": "127.0.0.1", "username": "root", "password": "root", "dbname": "test_space", "port": "3306"}

    # 创建表
    test_create_table(params)

    # 插入更新
    test_insert_update(params)
    # 单条查询的方法
    test_fetchone(params)
    # 多条查询的方法
    test_fetchall(params)
