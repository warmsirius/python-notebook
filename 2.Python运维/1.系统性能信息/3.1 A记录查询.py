# coding: utf-8
import dns.resolver


def run():
    domain = input("请输入主机名: ")
    A = dns.resolver.query(domain, "A")  # 如: www.baidu.com

    for i in A.response.answer:
        for j in i.items:
            # 增加 rdtype判断，只输出A类型的地址, A=1
            if j.rdtype == 1:
                print(j.address)
                # 请输入主机名: www.baidu.com
                # 110.242.68.3
                # 110.242.68.4


if __name__ == "__main__":
    run()
