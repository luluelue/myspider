# -*- coding: utf-8 -*-

# Scrapy settings for myspider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import datetime
import os

BOT_NAME = 'myspider'

SPIDER_MODULES = ['myspider.spiders']
NEWSPIDER_MODULE = 'myspider.spiders'

# 日志
LOG_ENCODING = 'utf-8'
LOG_LEVEL = "INFO"
LOG_FORMAT = '\x1b[0;0;34m%(asctime)s\x1b[0;0m \x1b[0;0;36m[%(name)s]\x1b[0;0m \x1b[0;0;31m%(levelname)s\x1b[0;3m: %(message)s'

# 显示cookie的传递过程日志
COOKIES_DEBUG = True

# to_day = datetime.datetime.now()
# log_file_path = 'D:/log/scrapy_{}_{}_{}.log'.format(to_day.year, to_day.month, to_day.day)
# if not os.path.isdir("D:/log/"):  # 无文件夹时创建
#             os.makedirs("D:/log/")
# if not os.path.isfile(log_file_path):  # 无文件时创建
#             fd = open(log_file_path, mode="w", encoding="utf-8")
#             fd.close()
# LOG_FILE = log_file_path

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'

# Obey robots.txt rules
# 是否遵守roboot协议文件
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 设置最大并发数，默认是16
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 设置两次下载之间的间隔，默认0
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# 域名最大并发数，和ip最大并发数
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 开启cookie
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# 是否开启Telnet插件
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# 设置请求头
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# 开启的中间件
# SPIDER_MIDDLEWARES = {
#    'myspider.middlewares.MyspiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# 开启的下载中间件
# DOWNLOADER_MIDDLEWARES = {
#    'myspider.middlewares.MyspiderDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# 开启的扩展
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# 开启的管道
ITEM_PIPELINES = {
    'myspider.pipelines.SunGvPipeline': 301,
}
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "sungv"
MONGODB_COLLECTION = "item"

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
