"""
===== 摩尔投票法进阶 =====
请利用"摩尔投票法"来找出数量最多的两个元素，而且这两个元素的数量还需要分别超过总数的三分之一
"""


def run(_list: list):
    count1 = count2 = 0
    ele1 = ele2 = _list[0]
    for i in _list:
        if i == ele1:
            count1 += 1
            continue
        elif i == ele2:
            count2 += 1
            continue
        elif count1 == 0:
            ele1 = i
            continue
        elif count2 == 0:
            ele2 = i
            continue
        else:
            count1 -= 1
            count2 -= 1
    if _list.count(ele1) >= len(_list)/3 and _list.count(ele2) >= len(_list)/3:
        print(f"数量最多的两个元素分别为{ele1}和{ele2}")

if __name__ == "__main__":
    _list = input("请输入元素, 各个元素之间以','分割: ").split(',')
    run(_list)


"""
0. 我们可以在同一轮循环中筛选出两个占比最多的元素
1. 首先我们可以先将最多的两个元素(ele1和ele2)都暂定为列表中第一个元素, 并将count计数(count1和count2)都设置为0, 然后再开始对列表循环
2. 对抗阶段:
    首先判断当前循环到的元素是否与ele1(ele2)相同
    如果相同, count1(count2)加1并直接通过continue开始循环下一个元素, 可以避免影响count2(count1)的计数
    当前循环到的元素如果与ele1和ele2都不相同时, 需要判断count1(count2)是否为0
    若为0, 将ele1(ele2)替换为当前循环到的元素并直接通过continue开始循环下一个元素, 可以避免影响ele2(ele1)
    如果当前循环到的元素如果与ele1和ele2都不相同且count1和count2都不为0, 为count1和count2同时减1
3. 计数阶段:
    此阶段循环已经结束, 我们需要判断所暂定的元素的占比是否分别超过所有元素的三分之一
"""
