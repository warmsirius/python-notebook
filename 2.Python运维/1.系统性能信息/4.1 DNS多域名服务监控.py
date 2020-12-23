# coding: utf-8

import dns.resolver
import http.client

IP_LIST = []  # 定义域名变量
APP_DOMAIN = "www.baidu.com"  # 定义业务域名


def get_ip_list(domain=""):
    try:
        A = dns.resolver.query(domain, "A")
    except Exception as e:
        print("dns resolver error:" + str(e))

    for i in A.response.answer:
        for j in i.items:
            # 增加 rdtype判断,只输出A类型的地址, A=1
            if j.rdtype == 1:
                IP_LIST.append(j.address)
    return True


def check_ip(ip):
    checkurl = ip + ":80"
    conn = http.client.HTTPConnection(checkurl, timeout=5)  # 创建http连接对象

    try:
        conn.request("GET", "/", headers={"Host": APP_DOMAIN})  # 发起URL请求,添
        r = conn.getresponse()
        getcontent = r.read(15)  # 获取URL页面前15个字符,如果需要做校验的话
    finally:
        if getcontent == b'<!DOCTYPE html>':  # 监控URL页的内容一般是事先定义好的,比如 status_code 或者 html页面
            print(ip + " [OK]")
        else:
            print(ip + " [Error]")  # 此处可放告警程序,可以是邮件、短信通知


if __name__ == "__main__":
    if get_ip_list(APP_DOMAIN) and len(IP_LIST) > 0:  # 条件:域名解析正确且至少返回一个IP
        for ip in IP_LIST:
            check_ip(ip)
    else:
        print("dns resolver error.")
