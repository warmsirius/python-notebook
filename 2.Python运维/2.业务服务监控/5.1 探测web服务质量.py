import os, sys

import pycurl

"""
HTTP服务是最流行的互联网应用之一，服务质量的好坏关系到用户体验以及网站的运营服务水平，最常用的有两个标准

1、服务的可用性，比如是否处于正常提供服务状态，而不是出现404页面未找到或500页面错误等
2、服务的响应速度，比如静态类文件下载时间都控制在毫秒级，动态CGI为秒级。

本示例使用 pycurl 的 setopt 与 getinfo 方法实现HTTP服务质量的探测。
1、获取监控URL返回的HTTP状态码，HTTP状态码采用pycurl.HTTP_CODE常量得到
2、HTTP请求到完成下载期间各环节的响应时间，通过pycurl.NAMELOOKUP_TIME、pycurl.CONNECT_TIME、pycurl.PRETRANSFER_TIME、pycurl.R等常量来实现。
3、通过pycurl.WRITEHEADER、pycurl.WRITEDATA常量得到目标URL的HTTP响应头部及页面内容
"""

URL = "https://www.baidu.com"  # 探测的目标URL

c = pycurl.Curl()  # 创建一个Curl对象

c.setopt(pycurl.URL, URL)  # 定义请求的URL常量
c.setopt(pycurl.CONNECTTIMEOUT, 5)  # 定义请求连接的等待时间
c.setopt(pycurl.TIMEOUT, 5)  # 定义请求超时时间
c.setopt(pycurl.NOPROGRESS, 1)  # 屏蔽下载进度条
c.setopt(pycurl.FORBID_REUSE, 1)  # 完成交互后强制断开连接,不重用
c.setopt(pycurl.MAXREDIRS, 1)  # 指定HTTP重定向的最大数为1
c.setopt(pycurl.DNS_CACHE_TIMEOUT, 30)  # 设置保存DNS信息的时间为30秒

# 创建一个文件对象,以 "wb" 方式打开,用来存储返回的http头部及页面内容
indexfile = open(os.path.dirname(os.path.realpath(__file__)) + "/content.txt", "wb")

c.setopt(pycurl.WRITEHEADER, indexfile)  # 将返回的HTTP HEADER定向到indexfile文件对象
c.setopt(pycurl.WRITEDATA, indexfile)  # 将返回的HTML内容定向到indexfile文件对象

try:
    c.perform()  # 提交请求
except Exception as e:
    print("connection error:" + str(e))

    indexfile.close()
    c.close()
    sys.exit()

NAMELOOKUP_TIME = c.getinfo(c.NAMELOOKUP_TIME)  # 获取DNS解析时间
CONNECT_TIME = c.getinfo(c.CONNECT_TIME)  # 获取建立连接时间
PRETRANSFER_TIME = c.getinfo(c.PRETRANSFER_TIME)  # 获取从建立连接到准备传输所消
STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)  # 获取从建立连接到传输开始消
TOTAL_TIME = c.getinfo(c.TOTAL_TIME)  # 获取传输的总时间
HTTP_CODE = c.getinfo(c.HTTP_CODE)  # 获取HTTP状态码
SIZE_DOWNLOAD = c.getinfo(c.SIZE_DOWNLOAD)  # 获取下载数据包大小
HEADER_SIZE = c.getinfo(c.HEADER_SIZE)  # 获取HTTP头部大小
SPEED_DOWNLOAD = c.getinfo(c.SPEED_DOWNLOAD)  # 获取平均下载速度

# 打印输出相关数据
print("HTTP状态码: %s" % (HTTP_CODE))
print("DNS解析时间: %.2f ms" % (NAMELOOKUP_TIME * 1000))
print("建立连接时间: %.2f ms" % (CONNECT_TIME * 1000))
print("准备传输时间: %.2f ms" % (PRETRANSFER_TIME * 1000))
print("传输开始时间: %.2f ms" % (STARTTRANSFER_TIME * 1000))
print("传输结束总时间: %.2f ms" % (TOTAL_TIME * 1000))
print("下载数据包大小: %d bytes/s" % (SIZE_DOWNLOAD))
print("HTTP头部大小: %d byte" % (HEADER_SIZE))
print("平均下载速度: %d bytes/s" % (SPEED_DOWNLOAD))

# 关闭文件及Curl对象
indexfile.close()
c.close()
