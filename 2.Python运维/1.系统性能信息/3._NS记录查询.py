# coding: utf-8
import dns.resolver


def run():
    domain = input("请输入主机名: ")

    # 指定查询类型为NS记录。
    # 注意: 只限输入一级域名，如baidu.com。如果输入二级或多级域名，如www.baidu.com，则是错误的。
    NS = dns.resolver.query(domain, "NS")  # 如: baidu.com

    for i in NS.response.answer:
        for j in i.items:
            print(j.to_text())
            # 请输入主机名: baidu.com
            # ns4.baidu.com.
            # ns7.baidu.com.
            # ns2.baidu.com.
            # dns.baidu.com.
            # ns3.baidu.com.


if __name__ == "__main__":
    run()
