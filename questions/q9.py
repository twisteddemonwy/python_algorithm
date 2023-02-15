"""
===== 凯撒加密奥义 =====
《罗马帝王传》中描述的凯撒大帝所使用的加密规则如下：
    将每个字母换成其在字母表中后移三位的字母，例如将字母 A换成字母 D; 字母 B换成字母 E
    以此类推，字母XYZ分别换成字母ABC
请问: 可以通过编程实现对字母的加密或者解密吗？
"""


def run(text: str, todo: str):
    new_text = ""
    for i in text:
        code = ord(i)
        if (65 <= code <= 90) or (97 <= code <= 122):
            if todo == "加密":
                new_code = code - 23 if (code+3 > 122) or (90 < code+3 < 97) else code+3
            else:
                new_code = code + 23 if (code-3 < 65) or (90 < code-3 < 97) else code-3
            new_text += chr(new_code)
        else:
            new_text += i
    return new_text


if __name__ == "__main__":
    text = input("请输入文字:")
    new_text = run(text, input("加密 or 解密？"))
    print(new_text)


"""
思路解析:
0. 我们可以利用ASCII码完成题目, A~Z的ASCII码为65~90, a~z的ASCII码为97~122
1. ord()可以将字符转为ASCII码
2. chr()可以将ASCII码转为字符
3. 因为大小写字母的ASCII码是两段分别连续的数字, 因此在加减3时需要注意边界
4. 加密时如果+3导致超出边界, 此时我们需要额外-26, 以次来循环26个字母, 即code+3-26=code-23
5. 解密时如果-3导致超出边界, 此时我们需要额外+26, 以次来循环26个字母, 即code-3+26=code+23
"""
