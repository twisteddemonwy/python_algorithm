"""
===== 黑洞数 =====
黑洞数: 任何一个数字不完全相同的整数, 在经过有限次”重排求差“操作后, 总会得到某一个或一些数，这些数即为黑洞数
重排求差: 指将组成一个数的各位数字重新排列，将得到的最大数减去最小数
例如207的重排求差操作: 720-027=693 963-369=594 954-459=495 此时再进行重排求差结果将不再改变, 我们称495就是黑洞数
题目如下:
    通过编程获得某个三位数对应的黑洞数
"""


def get_number_list(number):
    number_list = []
    while number >= 10:
        number_list.append(number % 10)
        number = number // 10
    number_list.append(number)

    return number_list


def get_max_number(number_list: list[int]):
    max_number = ""
    for _ in range(len(number_list)):
        max_number += str(number_list.pop(number_list.index(max(number_list))))

    return int(max_number)


def get_min_number(number_list: list[int]):
    min_number = ""
    for _ in range(len(number_list)):
        min_number += str(number_list.pop(number_list.index(min(number_list))))

    return int(min_number)


def run(num):
    max = get_max_number(get_number_list(num))
    min = get_min_number(get_number_list(int(num)))
    new = max - min
    while True:
        undetermined = new
        max = get_max_number(get_number_list(new))
        min = get_min_number(get_number_list(new))
        new = max - min

        if undetermined == new:
            print(new)
            break


if __name__ == "__main__":
    run(int(input("请输入一个三位数:")))


"""
思路解析:
0. 将我们得到的数字拆分
1. 把差分后的数字拼接成一个最大值(max)，一个最小值(min)
2. 得到最大值与最小值的差(new), 并将该值暂时保存到一个中间变量(undetermined)中
3. 将差值带入到步骤 0~2 中循环, 直到中间变量与新的差值相同(undetermined == new),跳出循环
4. 此时的差值即为黑洞数, 打印即可
"""
