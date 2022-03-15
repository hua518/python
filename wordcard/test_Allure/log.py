# # -*- coding: utf-8 -*-
# import logging
# #配置日志文件
#
# logging.basicConfig(
#     filename='example.log',#保存的文件名
#     level=logging.DEBUG,
#     datefmt='[%Y-%m-%d %H:%M:%S]',#日期格式
#     format='%(asctime)s %(levelname)s %(filename)s [%(lineno)d] %(threadName)s : %(message)s',#保存数据格式
#
#     )
#
# logging.debug('这个是调试时记录的日志信息')
# logging.info('程序正常运行时记录的日志信息')
# logging.warning('程序警告记录的信息')
# logging.critical("特别严重的问题")
# logging.error("程序错误时的记录，比如网络请求过慢等")


# -*- coding: utf-8 -*-
# @File      : log.py
# Create Time: 12/24/2019 10:16 AM
# Usage, put your example for your API
#
#
# Create by  : JunPing Ge
# changelog:
#
import logging
logger_name = 'example'
logger = logging.getLogger(logger_name)
logger.setLevel(logging.DEBUG)

log_path = 'C:\\Users\\MB\\Desktop\\log\\log.log'
file_handler = logging.FileHandler(log_path)
file_handler.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)

format_str = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(message)s"
date_format_str = "%Y-%m-%d %H:%M:%S"
formatter = logging.Formatter(format_str, date_format_str)

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
def info(name):
    return logger.info(name)
def debug(name):
    return logger.debug(name)
def warning(name):
    return logger.warning(name)
def error(name):
    return logger.error(name)
def critical(name):
    return logger.critical(name)
# logger.debug('debug message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')