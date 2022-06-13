from pymysql import *

# -*- coding:utf-8 -*-
mydb = connect(
    host='192.168.43.91',
    port=3306,
    user='root',
    password='123456Yh@wei',
    db='mysql',
    charset='utf8'
)


def add_users(m):
    mydb = connect(
        host='192.168.43.91',
        port=3306,
        user='root',
        password='123456Yh@wei',
        db='mysql',
        charset='utf8'
    )
    users_ = []
    cs = mydb.cursor()  # 获取光标
    with open("test.txt", 'r') as fr:
        # 读取文件所有内容
        arrayOLines = fr.readlines()
    for line in arrayOLines:
        # s.strip(rm)，当rm空时,默认删除空白符(包括'\n','\r','\t',' ')
        line = m+'\t'+line.strip()
        # 使用s.split(str="",num=string,cout(str))将字符串根据'\t'分隔符进行切片。
        users_ = users_+[tuple(line.split('\t'))]
    n = tuple(users_)
    cs.executemany("insert into `test_copy1` values(%s,%s,%s,%s,%s,%s,%s,%s)",n)
    # cs.executemany("insert into user values(%s)",m)
    mydb.commit()
    cs.close()
    mydb.close()

# import pandas as pd
#
# data = pd.read_csv('result.csv', encoding='utf8')
# with open('test1.txt', 'a+') as f:
#     for line in data.values:
#         f.write((str(line[0]) + '\t' + str(line[1]) + '\t' + str(line[2]) + '\t' + str(line[3]) + '\t' + str(
#             line[4]) + '\t' + str(line[5]) + '\t' + str(line[6]) + '\t' + str(line[7]) + '\t' + str(line[8]) + '\n'))
