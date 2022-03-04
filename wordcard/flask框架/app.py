
import os
import pymysql
from dotted_dict import DottedDict
import pytest
import requests
from Lib import json
from flask import Flask,request

app=Flask(__name__)
@app.route("/",methods=['get','post'])
#####......................flask方案1...................................#####
# def hello():
#     text = "谢婧是大美女"
#
#     # jsontext = json.dumps(text) //输出成json格式coding: utf - 8
#     # return jsontext
#     return text
# if __name__=='_main_':
#     app.run()
#####......................flask方案1...................................#####

#####......................flask方案2...................................#####
def indextest():
    inputData = request.headers.get("inputData")
    data = getconnectmysql(inputData)
    return data
def getconnectmysql(inputData):
    connect = pymysql.connect(host = '127.0.0.1',user = 'root',passwd = '123456',port = 3306, db = 'test',charset = 'utf8')
    cur = connect.cursor()  #生成游标对象
    if inputData ==True:
        sql = "select Dno,DName,DHost From department where DName = '%s'" % (inputData)
    sql= "select * From department"

    cur.execute(sql) #执行数据库语句
    data = cur.fetchall() #获取数据
    para = []
    for i in data:
        # print(i)
        text = {'DNo':i[0],'DName':i[1],'DHost':i[2]}
        para.append(text)
    # cur.close()
    return json.dumps(para,ensure_ascii=False,indent=4)
if __name__=='_main_':
    app.run()
#####......................flask方案2...................................#####
def sys():
    os.system("flask run -h 127.0.0.1 -p 5000")#函数名需要为app.py,不然无法使用，参考印象笔记
sys()