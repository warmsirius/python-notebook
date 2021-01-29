# -*- coding: utf-8 -*-

import os, sys, time, subprocess
from scapy.as_resolvers import AS_resolver_radb
from scapy.all import traceroute

import warnings, logging

warnings.filterwarnings("ignore", category=DeprecationWarning)  # 屏蔽scapy无用告警信息

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)  # 屏蔽模块IPv6多余告警

domains = input('Please input one or more IP/domain: ')  # 接受输入的域名或IP

target = domains.split(' ')

dport = [80, 443]  # 扫描的端口列表

if len(target) >= 1 and target[0] != '':
    # 启动路由跟踪
    res, unans = traceroute(target, dport=dport, retry=-2)  # 启动路由跟踪

    # res.graph(target="> test.svg")  # 生成svg矢量图形
    # ASres=AS_resolver_radb()改变为可用的whois提供商,而非原来的ASres=None后默认的被qiang了的提供商
    res.graph(target="> test.svg", ASres=AS_resolver_radb(), type="svg")
    time.sleep(1)

    # svg 转格式为 png
    subprocess.Popen("/usr/bin/convert test.svg test.png", shell=True)  # svg转png格式
else:
    print("IP/domain number of errors,exit")
