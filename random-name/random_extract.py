import random
from contextlib import nullcontext


def get_text_at_line(file_name, line_number):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()
            return lines[line_number - 1].strip()  # 行号从1开始，列表索引从0开始
    except FileNotFoundError:
        print(f"文件 {file_name} 不存在.")
        return None
    except IndexError:
        print(f"文件 {file_name} 中没有找到第 {line_number} 行.")
        return None


def generate_random_numbers(max: int):
    random.seed()  # 只需要在真正需要随机的时候调用 seed() 就可以了，不需要每次函数调用都调用
    in_list = list(range(max))  # 使用 list 和 range 生成数字列表
    random.shuffle(in_list)  # 使用 random 的 shuffle 方法打乱列表顺序
    return in_list


def get_random_result(num: int, max: int):
    try:
        with nullcontext(FileNotFoundError):  # 如果文件不存在，直接抛出异常，由上层处理
            out_list = generate_random_numbers(max)
        out_list = [
            get_text_at_line("抽取列表.txt", i) for i in out_list
        ]  # 使用列表推导式读取每一行的内容
        return out_list[:num]  # 返回指定索引位置的结果
    except IndexError as e:
        print(f"获取随机结果时出错：{e}")
        return None


if __name__ == "__main__":
    print(get_random_result(2, 54))
