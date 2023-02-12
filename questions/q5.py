"""
===== 与谁结婚 =====
已知：有三对情侣要结婚；
     三位男士分别为A，B，C；
     三位女士分别为X，Y，Z；
     现有三对新人为你出题希望你可以正确为他们配对：
        1. A说自己要和X结婚
        2. X说他的未婚夫是C
        3. C说他要和Z结婚
请问：假设上述新人所言都为错误，那么你可以正确为他们配对吗？
"""


boys = ["A", "B", "C"]
for X in boys:
    for Y in boys:
        for Z in boys:
            if X != boys[0] and X != boys[2] and Z != boys[2] and X != Y != Z != X:
                print("X与{}配对，Y与{}配对，Z与{}配对".format(X, Y, Z))


"""
思路解析：
1. 假设女士为变量X，Y，Z
2. 假设男士为值"A"，"B"，"C"
3. 由于三位说的都是假话因此我们可以初步得出一些结论：
    A不与X配对: X != "A"
    C不与X配对: X != "C"
    C不与Z配对: Z != "C"
4. 同时男士与女士应该一一配对，不可能出现多选的情况,因此：
    X != Y and Y != Z and Z != X 
"""
print("========== 分割线 ==========")


for X in ["B", "C"]:
    for Z in ["A", "B", "C"]:
        if X != "C" != Z != X:
            print("X与{}配对，Y与C配对，Z与{}配对".format(X, Z))


"""
优化思路:
通过题面我们可以缩小循环范围：
    A不与X配对: 此时X只需要在["B", "C"]中循环
    C不与X配对并且C不与Z配对: 此时C已经确定了配对情况，即：Y="C"
"""