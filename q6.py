"""
===== 谁在说谎 =====
已知：现在有A，B，C
        A说B在说谎
        B说C在说谎
        C说A和B两人都在说谎
请问：到底谁说的是真话谁说的是假话
"""


for a in range(2):
    for b in range(2):
        for c in range(2):
            if (
                ((a and not b) or (not a and b))
                and ((b and not c) or (not b and c))
                and ((c and not a and not b) or (not c and (a or b)))
            ):
                a = "真" if a == 1 else "假"
                b = "真" if b == 1 else "假"
                c = "真" if c == 1 else "假"
                print("A说的是{}话\nB说的是{}话\nC说的是{}话".format(a, b, c))


"""
思路解析：
1. 对题目中的三个条件逐一进行真假假设,会有以下结果
    假设A说的是真话：a and not b
    假设A说的是假话：not a and b
    假设B说的是真话：b and not c
    假设B说的是假话：bot b and c
    假设C说的是真话：c and not a and not b
    假设C说的是假话：not c and (a or b)
2. 因为一个人说的话要么为真要么为假，因此对于同一人的两种假设之间用or，不同人之间用and
"""
