"""
===== 百钱百鸡 =====
已知：一只公鸡5元；
     一直母鸡3元；
     3只小鸡1元。
请问：先要用100元买100只小鸡，公鸡母鸡小鸡各能买多少只？
"""


for cock in range(21):
    for hen in range(33):
        for chick in range(101):
            if (cock + hen + chick) == 100 and ((5 * cock) + (3 * hen) + (chick / 3)) == 100:
                print(f"可购买公鸡{cock}只，母鸡{hen}只，小鸡{chick}只")
"""
思路解析:
1. 我们可以通过最极端的方式计算出三种类型的鸡可购买的数量范围
    当100都用来买公鸡时，最多可购买20只
    当100都用来买母鸡时，最多可购买33只
    当100都用来买小鸡时，最多可购买100只
2. 通过穷举法遍历所有组合的可能，并对每一个组合进行条件判断（共有100只鸡并且总金额为100元）
    公鸡：0~20只
    母鸡：0~33只
    小鸡：0~100只
"""
print("========== 分割线 ==========")


for cock in range(21):
    for hen in range(33):
        chick = 100 - cock - hen
        if ((5 * cock) + (3 * hen) + (chick / 3)) == 100:
            print(f"可购买公鸡{cock}只，母鸡{hen}只，小鸡{chick}只")

"""
优化思路:
当我们进行第一次和第二次循环时可以既可以获得公鸡和母鸡的数量
又因为我们总共需要100只鸡
那么此时的小鸡数量必然为公鸡母鸡数量和与100的差值

所以我们可以去掉第三层对于小鸡数量的循环
同样可以去掉判断中数量和为100的条件
"""
