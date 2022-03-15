
from dotted_dict import DottedDict as Dot
import requests
import json
import xlrd
from contextlib import closing
from requests import exceptions
##########################单词搜索###############################
def serchword():
    url = "http://mo-miaobao-mb.suanshubang.cc/studyen/wordcard/searchwords"
    params = {
        "words":"goods"
    }
    default = {'Content-Type': 'application/json'}
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='GB18030')
    response1 = requests.patch(url, data=json.dumps(params), headers=default)
    print(json.dumps(response1.json(), indent=2, ensure_ascii=False))
    response = requests.post(url,data=json.dumps(params),headers=default)

    json_w = json.loads(response.content)
    json_w["errstr"] = "shibai"
    print(json_w)

    # re=DottedDict(response.json())
    # print(re)
    # print(response.json())
    print(json.dumps(json_w,indent=2,ensure_ascii=False))
    response= Dot(response.json())
#
##########################单词搜索###############################



 ####################################下载流，图片下载##################################
def download_image_improve():
    url = "https://images2017.cnblogs.com/blog/1278509/201711/1278509-20171114131843031-132422801.png"
    response = requests.get(url, stream=True)
    chunk_size = 1024  # 单次请求最大值
    content_size = int(response.headers['content-length'])  # 内容体总大小
    data_count = 0
    with closing(requests.get(url, stream=True)) as response:
        # 这里打开一个空的png文件，相当于创建一个空的txt文件,wb表示写文件
        with open('selenium1.png', 'wb') as file:
            # 每128个流遍历一次
            for data in response.iter_content(128):
                # 把流写入到文件，这个文件最后写入完成就是，selenium.png
                file.write(data)
                data_count = data_count + len(data)
                now_jd = (data_count / content_size) * 100
                print("\r 文件下载进度：%d%%(%d/%d) - %s" % (now_jd, data_count, content_size, url), end=" ")

####################################下载流，图片下载##################################


#################################读取excel######################################
def get_data(filename, sheetnum):
    dir_case = 'case.xls'
    data = xlrd.open_workbook(dir_case)
    table = data.sheets()[sheetnum]
    nor = table.nrows
    nol = table.ncols
    dict = {}
    for i in range(1, nor):
        for j in range(nol):
            title = table.cell_value(0, j)
            value = table.cell_value(i, j)
            dict[title] = value
        yield dict
if __name__ == '__main__':
    for i in get_data('add_user', 0):
        print(i)
#################################读取excel######################################

serchword()             ####搜索单词
download_image_improve()####下载图片