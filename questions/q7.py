"""
===== 字符串测试 =====
判断给定的字符串中括号的写法是否合法
约束条件：字符串仅包含：() [] {} 三种括号的组合
        左右括号必须成对编写
        左右括号必须以正确的顺序编写，例如 "{(})"是不合法的
"""


_str = input("输入想要进行判断的字符串: ")
brackets = ["(", ")", "[", "]", "{", "}"]
get_brackets = []

for i in _str:
    if i not in brackets:
        continue
    if i == brackets[0] or i == brackets[2] or i == brackets[4]:
        get_brackets.append(i)
    else:
        if len(get_brackets) == 0:
            print("非法字符串")
            break
        if i == ")":
            get_f = get_brackets.pop()
            _f = brackets[0]
            if _f != get_f:
                print("非法字符串")
                break
        if i == "]":
            get_f = get_brackets.pop()
            _f = brackets[2]
            if _f != get_f:
                print("非法字符串")
                break
        if i == "}":
            get_f = get_brackets.pop()
            _f = brackets[4]
            if _f != get_f:
                print("非法字符串")
                break
else:
    if len(get_brackets) == 0:
        print("合法")
    else:
        print("非法字符串")


"""
思路解析：
0. 首先我们要清楚判断括号是否成对需要利用到栈（先进后出, 放到本题即为最先出现的左括号将最后出现其对应的右括号，例: ([{}])）
1. 因此我们需要创建一个空列表<get_brackets>，我们需要把该列表当作栈来使用
2. 对输入的字符串进行循环
3. 如果当前循环到的字符不是括号直接跳过
4. 如果当前循环到的字符是三种括号其一的左括号时，将该字符添加到<get_brackets>末尾
5. 如果当前循环到的字符是三种括号其一的右括号时, 我们需要判断<get_brackets>是否为空
   若为空证明这是一个只有右括号的组合形式
6. 如果当前循环到的字符是三种括号其一的右括号且<get_brackets>不为空时，我们将从<get_brackets>末尾取出一个字符
7. 判断当前循环到的字符是否与<get_brackets>末尾取出的字符是同类型括号
   如果不相同证明左右括号并不是以正确的顺序编写
8. 当字符串中所有字符都循环结束之后，需要判断<get_brackets>是否为空
   若不为空证明有至少一个括号是只有左括号的组合形式
"""
