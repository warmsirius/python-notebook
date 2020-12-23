import filecmp

if __name__ == "__main__":
    dir1 = "/Users/yuanjun/Documents/priv_repo/python-notebook/2.Python运维/2.业务服务监控/dir1"
    dir2 = "/Users/yuanjun/Documents/priv_repo/python-notebook/2.Python运维/2.业务服务监控/dir2"
    print(filecmp.cmpfiles(dir1, dir2, ["a.txt", "b.txt"]))
    # 输出:
    # (['a.txt'], ['b.txt'], [])

    print(filecmp.cmpfiles(dir1, dir2, ["a.txt", "b.txt"], shallow=False))
    # 输出
    # (['a.txt'], ['b.txt'], [])
