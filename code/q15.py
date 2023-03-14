"""
===== 素数 =====
素数: 只能被1和它自身整除的数叫做素数
题目如下:
    求出给定范围start~end之间的所有素数
"""


from math import sqrt

start = int(input("start: "))
end = int(input("end: "))

while start <= end:
    s = 2
    e = sqrt(start)
    flag = 1
    while s <= e:
        if start % s == 0:
            flag = 0
            break
        s += 1

    if flag == 1:
        print(f"{start}", end=" ")
    start += 1


"""
思路解析与优化:
0. 我们需要进行两层循环, 外层循环start~end获得待判断的值, 内层循环判断该值是否为素数
1. 外层循环范围即为start~end
2. 内层循环范围我们可以做优化, 优化之前我们需要了解合数的概念
    合数: 在大于1的整数中除了能被1和本身整除之外海能被其他的数(0除外)整除
    因此合数可以拆分成两个因数相乘, 这两个因数一定是一个小于等于√合数, 另一个大于等于√合数
    例如: 16=2*8, 16=4*4 16=8*2
    因此我们的内层循环只需要判断2~ √带判断数 即可, 如果中间出现余数为零的情况, 立退出该次内层循环即可
    python中可以使用math下的sqrt实现开平方运算
3. 循环中可以设置一个变量flag来控制输出
"""
