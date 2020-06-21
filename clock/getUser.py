#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql


def getUser():
    # 连接数据库
    conn = pymysql.connect(
        host='xxxxx',
        port=3306,
        user='root',
        password='123456',
        db='daka'
    )

    # 创建游标
    cur = conn.cursor()
    # 查询 账号、密码、邮箱
    cur.execute('select * from user_msg')
    # 获取数据
    msg = cur.fetchall()

    cur.close()
    conn.close()

    return msg

# if __name__ == '__main__':
#     print(getUser())
