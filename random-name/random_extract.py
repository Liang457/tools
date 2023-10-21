import random


def filter_lists(A: list, B: list):
    B_set = set(B)
    outlist = [i for i in A if i not in B_set]
    return outlist


def read_file_to_list():
    # 将抽取列表转换为一个列表
    with open("抽取列表.txt", encoding="utf-8") as file:
        list_from_file = [line.strip() for line in file]
    return list_from_file


def get_random_result(num: int):
    # 不去掉上次抽取的随机
    random.seed()
    # 读取文件
    name_list = read_file_to_list()
    # 打乱
    random.shuffle(name_list)
    # 输出
    return name_list[:num]


def get_random_result_rmlast(num: int, lastlist: list):
    # 去掉上次抽取的随机
    random.seed()
    # 读取文件
    name_list = read_file_to_list()
    # 去掉上一次
    name_list = filter_lists(name_list, lastlist)
    if len(name_list) != 0:
        # 打乱
        random.shuffle(name_list)
        if len(name_list) >= num:
            # 输出
            return name_list[:num]
        else:
            return name_list
    else:
        return ["已经抽完人了，请点击“排除已经抽过的人”重置"]


if __name__ == "__main__":
    print(get_random_result(2))
