#!/usr/bin/python3
import allure
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.exmail.qq.com"  # 设置服务器
mail_user = "yihua.zhong@paperang.com"  # 用户名
mail_pass = "Huahua6557098"  # 口令

sender = 'yihua.zhong@paperang.com'
receivers = ['1054555086@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')#无附件时可使用，只写入文字

message = MIMEMultipart()# 创建一个带附件的实例
subject = 'Python SMTP 邮件测试'#邮件发送的标题
message['From'] = Header("菜鸟教程", 'utf-8')#from_addr: 邮件发送者地址。


message['To'] = Header("测试", 'utf-8')#to_addrs: 字符串列表，邮件发送地址。

message['Subject'] = Header(subject, 'utf-8')
# 邮件正文内容
message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))#邮件发送的消息

# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('C:\\Users\\MB\\Desktop\\p\\logcat.txt', 'rb').read(), 'base64', 'utf-8')#这是保存在本地的文件
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="test.txt"'
message.attach(att1)

# 构造附件2，传送当前目录下的 runoob.txt 文件
att2 = MIMEText(open('jmeter.txt', 'rb').read(), 'base64', 'utf-8')#这是保存在文件目录下的文件
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
message.attach(att2)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")

