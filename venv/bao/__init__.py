# -*- coding = utf-8 -*-
# @Time :
# @ Author : Yeeero
# @File : __init__.py.by
# @Software : PyCharm
import pymysql


CONFIG={
    'host':'127.0.0.1',
    'port':'3306',
    'user':'root',
    'password':'root',
    'charset':'utf8'
}

class DB():
    def __init__(self):
        self.conn = pymysql.connect(**CONFIG)

    def __enter__(self):    # 在使用with语句时调用，会话管理器在代码块开始前调用，返回值与as后的参数绑定
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):  # 会话管理器在代码块执行完成好后调用，在with语句完成时，对象销毁之前调用
        if exc_type:
            self.conn.rollback()
        else:
            self.conn.commit()