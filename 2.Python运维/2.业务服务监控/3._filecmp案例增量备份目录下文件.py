import filecmp
import os, sys
import re
import shutil

holderlist = []


def compareme(dir1, dir2):
    """递归获取更新项函数"""
    dircomp = filecmp.dircmp(dir1, dir2)
    # 源目录新文件或目录
    only_in_one = dircomp.left_only
    # 不匹配文件，源目录文件已经发生变化
    diff_in_one = dircomp.diff_files
    # 定义源目录绝对路径
    dir_path = os.path.abspath(dir1)

    # 将更新文件名或目录追加到 holderlist
    [holderlist.append(os.path.join(dir_path, x)) for x in only_in_one]
    [holderlist.append(os.path.join(dir_path, x)) for x in diff_in_one]

    # 判断是否相同子目录，以便递归
    if len(dircomp.common_dirs) > 0:
        for item in dircomp.common_dirs:
            compareme(os.path.abspath(os.path.join(dir1, item)), os.path.abspath(os.path.join(dir2, item)))
    return holderlist


def main():
    import pdb; pdb.set_trace()
    if len(sys.argv) > 2:
        dir1 = sys.argv[1]
        dir2 = sys.argv[2]
    else:
        print("Usage: ", sys.argv[0], "datadir backupdir")
        sys.exit()

    # 获取要更新的目标文件
    source_files = compareme(dir1, dir2)
    dir1 = os.path.abspath(dir1)

    if not dir2.endswith("/"):
        dir2 += "/"
    dir2 = os.path.abspath(dir2)

    destination_files = []
    createdir_bool = False
    for item in source_files:
        # 将源目录差异路径清单对应替换成备份目录
        destination_dir = re.sub(dir1, dir2, item)
        destination_files.append(destination_dir)
        # 如果差异路径为目录且不存在，则在备份目录中创建
        if os.path.isdir(item):
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
                createdir_bool = True

    # 重新调用compareme函数，重新遍历新创建目录的内容
    if createdir_bool:
        destination_files = []
        source_files = []
        source_files = compareme(dir1, dir2)

        # 获取源目录差异路径清单，对应替换成备份目录
        for item in source_files:
            destination_dir = re.sub(dir1, dir2, item)
            destination_files.append(destination_dir)

    print("Update item:")
    print(source_files)
    copy_files = zip(source_files, destination_files)
    for item in copy_files:
        # 判断是否为文件，进行复制操作
        if os.path.isfile(item[0]):
            shutil.copyfile(item[0], item[1])


if __name__ == "__main__":
    main()
    # 终端执行命令
    # python 2._filecmp.dircmp校验源与备份目录差异.py /Users/yuanjun/Documents/priv_repo/python-notebook/2.Python运维/2.业务服务监控/dir1 /Users/yuanjun/Documhon-notebook/2.Python运维/2.业务服务监控/dir3
