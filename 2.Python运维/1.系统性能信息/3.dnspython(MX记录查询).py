# coding: utf-8
import dns.resolver


def run():
    domain = input("请输入主机名: ")
    # 仅限输入邮件服务器的域名
    MX = dns.resolver.query(domain, "MX")  # 如: 163.com

    for i in MX:
        print("MX preference =", i.preference, "mail exchanger=", i.exchange)
        # 请输入主机名: 163.com
        # MX preference = 10 mail exchanger= 163mx03.mxmail.netease.com.
        # MX preference = 50 mail exchanger= 163mx00.mxmail.netease.com.
        # MX preference = 10 mail exchanger= 163mx01.mxmail.netease.com.
        # MX preference = 10 mail exchanger= 163mx02.mxmail.netease.com.


if __name__ == "__main__":
    run()
