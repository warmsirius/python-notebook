import filecmp

if __name__ == "__main__":
    dir1 = "/Users/yuanjun/Documents/priv_repo/python-notebook/2.Python运维/2.业务服务监控/dir1"
    dir2 = "/Users/yuanjun/Documents/priv_repo/python-notebook/2.Python运维/2.业务服务监控/dir2"
    # 目录比较，忽略test.txt文件
    dirobj = filecmp.dircmp(dir1, dir2, ignore=["test.txt"])

    # 输出对比结果数据报表
    print("---------------------report------------------------")
    dirobj.report()

    print("--------------report_partial_closure---------------")
    dirobj.report_partial_closure()

    print("---------------report_full_closure-----------------")
    dirobj.report_full_closure()

    print("===================================================")
    print("left_list:  " + str(dirobj.left_list))
    print("right_list:  " + str(dirobj.right_list))
    print("common:  " + str(dirobj.common))

    print("===================================================")
    print("left_only:  " + str(dirobj.left_only))
    print("right_only:  " + str(dirobj.right_only))
    print("common_dirs:  " + str(dirobj.common_dirs))

    print("===================================================")
    print("common_files:  " + str(dirobj.common_files))
    print("common_funny:  " + str(dirobj.common_funny))

    print("===================================================")
    print("same_files:  " + str(dirobj.same_files))
    print("diff_files:  " + str(dirobj.diff_files))
    print("funny_files:  " + str(dirobj.funny_files))
    print("===================================================")
