"""
===== 哥德巴赫猜想 =====
哥德巴赫猜想: 任意大于2的偶数, 都可以表示成两个素数之和, 例如8=5+3, 12=7+5
题目如下:
    求证2333以内的不小于4的正偶数都能够分解为两个素数之和
"""
from math import sqrt


def prime_num(number: int):
    e = int(sqrt(number))+1
    for i in range(2, e):
        if number % i == 0:
            return False
    return True


def guess(n: int):
    if n % 2 != 0:
        return "所输入数字并非偶数"

    for i in range(2, int(n/2)+1):
        if i != 2 and i % 2 == 0:
            continue

        if prime_num(i):
            if prime_num(n-i):
                return (i, n-i)

    return "哥德巴赫猜想验证失败"


if __name__ == "__main__":
    result = guess(int((input("请输入4~2333之间的偶数: "))))
    print(result)


"""
思路解析与优化:
0. 首先我们要明确两数之和a+b=n中a和b的取值范围相同并且都是小于等于1/2n的, 因此我们的循环范围为0~n//2
1. 又由于素数的性质，因此0, 1 以及大于2的偶数都不包含在判断范围内，可以跳过
2. 判断循环到的数a是否为素数，若为素数继续判断n-a是否为素数
3. 若a 与 n-a 都为素数中断循环返回即可，证明哥德巴赫猜想是正确的
4. 若直到循环结束还没有找到两个素数的和，证明哥德巴赫猜想的是失败的
"""
