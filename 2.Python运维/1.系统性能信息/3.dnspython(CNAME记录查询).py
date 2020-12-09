# coding: utf-8
import dns.resolver


def run():
    domain = input("请输入主机名: ")

    # 指定查询类型为 CNAME记录。
    # cname的解析过程：是local dns server把cname直接解析成ip。
    # 而不是 dns resolver先请求cname拿到被指向的域名，再做一次dns请求解析到ip。
    # 对于nslookup、dig工具，会解析成cname所指向的域名，而不是直接到ip。
    CNAME = dns.resolver.query(domain, "CNAME")  # 如: img.taobao.com

    for i in CNAME.response.answer:
        for j in i.items:
            print(j.to_text())
            # 请输入主机名: img.taobao.com
            # img.taobao.com.danuoyi.tbcache.com.


if __name__ == "__main__":
    run()
