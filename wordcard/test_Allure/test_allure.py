import os
import allure
import logging

import pymysql

import pytest
import requests
import  sys
import  io
from Lib import json

from pytest_assume.plugin import assume



from contextlib import closing

from requests import exceptions

#
# def test_serchword():
#     url = "http://10.66.0.202:8020/studyen/wordcard/searchwords"
#     params = {
#         "words":"goods"
#     }
#     default = {'Content-Type': 'application/json'}
#     # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='GB18030')
#     response1 = requests.patch(url, data=json.dumps(params), headers=default)
#     print(json.dumps(response1.json(), indent=2, ensure_ascii=False))
#     response = requests.post(url,data=json.dumps(params),headers=default)
#
#     json_w = json.loads(response.content)
#     json_w["errstr"] = "shibai"
#     print(json_w)
#
#     # re=DottedDict(response.json())
#     # print(re)
#     # print(response.json())
#     print(json.dumps(json_w,indent=2,ensure_ascii=False))
# test_serchword()
# #
# def download_image_improve():
#     url = 'https://images2017.cnblogs.com/blog/1278509/201711/1278509-20171114131843031-132422801.png'
#     response = requests.get(url, stream=True)
#     with closing(requests.get(url, stream=True)) as response:
#         # 这里打开一个空的png文件，相当于创建一个空的txt文件,wb表示写文件
#         with open('selenium1.png', 'wb') as file:
#             # 每128个流遍历一次
#             for data in response.iter_content(128):
#                 # 把流写入到文件，这个文件最后写入完成就是，selenium.png
#                 file.write(data)




# test_serchword()
# download_image_improve()
@pytest.mark.p0
def test_one():
    print("\n输出第一个结果")
@pytest.mark.p0
def test_two():
    print("输出第二个结果")
    # try:
    #     h=0
    #     assert (h==0)
    # except exceptions as e:
    #     print("1")
    #     raise e

def test_thre():
    h=1
    assert(h == 1)

if __name__ =="__main__":
    pytest.main(['-s'])
###################执行生成报告#########################
# os.system("pytest test_Allure --alluredir ./result/")     #####生成result的文件夹并执行allure#########
# os.system("allure generate ./result/ -o ./result/report/ --clean")######执行生成报告############




