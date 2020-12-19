import filecmp

if __name__ == "__main__":
    print(filecmp.cmp(
        "/Users/yuanjun/Documents/priv_repo/python-notebook/2.Python运维/2.业务服务监控/1.例-对比Nginx配置文件差异.py",
        "/Users/yuanjun/Documents/priv_repo/python-notebook/2.Python运维/2.业务服务监控/1.difflib-文件内容差异对比.md"))

    print(filecmp.cmp(
        "/Users/yuanjun/Documents/priv_repo/python-notebook/2.Python运维/2.业务服务监控/1.例-对比Nginx配置文件差异.py",
        "/Users/yuanjun/Documents/priv_repo/python-notebook/2.Python运维/2.业务服务监控/1.difflib-文件内容差异对比.md",
        shallow=False))
