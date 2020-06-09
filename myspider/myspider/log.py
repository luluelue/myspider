# coding=utf-8
import logging

# 日志配置
logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s [%(filename)s:%(line)d]'
                           ':  %(message)s'
                           ' - %(asctime)s',
                    datefmt='[%d/%b/%Y %H:%M:%S]')
