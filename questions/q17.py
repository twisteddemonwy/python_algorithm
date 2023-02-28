"""
===== 梅森素数 =====
梅森数: 形如2^n-1的正整数
梅森素数: 若2^n-1的结果为素数时, 就称之为梅森素数
题目如下:
    求出当n小于22时所有的梅森素数
"""


from math import sqrt


def prime_num(number: int):
    end = int(sqrt(number))+1
    flag = 1
    for i in range(2, end):
        if number % i == 0:
            flag = 0
            break
    if flag == 1:
        return 1


if __name__ == "__main__":
    for n in range(1, 23):
        number = (2**n)-1
        if prime_num(number):
            print(number)


"""
思路解析与优化:
0. 实现一个判断素数的方法prime_num, 具体实现方式请参照 q15
1. 对n的取值范围进行for循环
2. 求出梅森数的值, 并传递给prime_num函数判断, 若为素数print即可
"""
