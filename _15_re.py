import re

# re.compile(编译)
# re.match(从头找一个)
# re.search(找一个)
# re.findall(找所有)
# re.sub(替换)

# 字符 直接写在表达式内
# . 匹配所有 默认不匹配"\n"
r = re.findall(".", "\n")
print(r)
# 下列方式匹配"\n"
r = re.findall(".", "\n", re.DOTALL)
print(r)
r = re.findall(".", "\n", re.S)
print(r)
#
r = re.findall("\.", ".")
print(r)
# []
r = re.findall("a[bcd]e", "abcdeaceadeabe")  # 只能取方括号中间的值一次
print(r)  # ['ace', 'ade', 'abe']
r = re.findall("a[bcd]+e", "abcdeacccddceadeabe")  # 只能取方括号中间的值多次
print(r)  # ['abcde', 'ace', 'ade', 'abe']
r = re.findall("abe|ace|ade", "abcdeacccddceadeabe")  # 或者
print(r)  # ['ade', 'abe']

# 预定义字符集 写在[]中
r = re.findall("\d", "abcdeacccddceadeabe1234")  # 数字
print(r)  # ['1', '2', '3', '4']
r = re.findall("[0-9]", "abcdeacccddceadeabe1234")  # 数字
print(r)  # ['1', '2', '3', '4']
r = re.findall("\d+", "abcdeacccddceadeabe1234")  # 数字
print(r)  # ['1234']
r = re.findall("\D", "abcdeacccddceadeabe1234")  # 非数字
print(r)  # ['a', 'b', 'c', 'd', 'e', 'a', 'c', 'c', 'c', 'd', 'd', 'c', 'e', 'a', 'd', 'e', 'a', 'b', 'e']
r = re.findall("[^\d]", "abcdeacccddceadeabe1234")  # 非数字
print(r)  # ['a', 'b', 'c', 'd', 'e', 'a', 'c', 'c', 'c', 'd', 'd', 'c', 'e', 'a', 'd', 'e', 'a', 'b', 'e']
r = re.findall("[\s]", "abcde   acccddcea   deabe1234")  # 空白字符
print(r)  # [' ', ' ', ' ', ' ', ' ', ' ']
r = re.findall("[< >\t\r\n\f\v]", "abcde   acccddcea   deabe1234")  # 空白字符
print(r)  # [' ', ' ', ' ', ' ', ' ', ' ']
r = re.findall("[\S]", "abcde   acccddcea   deabe1234")  # 非空白字符
print(
    r)  # ['a', 'b', 'c', 'd', 'e', 'a', 'c', 'c', 'c', 'd', 'd', 'c', 'e', 'a', 'd', 'e', 'a', 'b', 'e', '1', '2', '3', '4']
r = re.findall("[^\s]", "abcde   acccddcea   deabe1234")  # 非空白字符
print(
    r)  # ['a', 'b', 'c', 'd', 'e', 'a', 'c', 'c', 'c', 'd', 'd', 'c', 'e', 'a', 'd', 'e', 'a', 'b', 'e', '1', '2', '3', '4']
r = re.findall("[\w]", "abcde ``  acccdd%%cea  $$ deabe1234+++###")  # 单词字符
print(
    r)  # ['a', 'b', 'c', 'd', 'e', 'a', 'c', 'c', 'c', 'd', 'd', 'c', 'e', 'a', 'd', 'e', 'a', 'b', 'e', '1', '2', '3', '4']
r = re.findall("[A-Za-z0-9_]", "abcde ``  acccdd%%cea  $$ deabe1234+++###")  # 单词字符
print(
    r)  # ['a', 'b', 'c', 'd', 'e', 'a', 'c', 'c', 'c', 'd', 'd', 'c', 'e', 'a', 'd', 'e', 'a', 'b', 'e', '1', '2', '3', '4']
r = re.findall("[\W]", "abcde ``  acccdd%%cea  $$ deabe1234+++###")  # 单词字符
print(r)  # [' ', '`', '`', ' ', ' ', '%', '%', ' ', ' ', '$', '$', ' ', '+', '+', '+', '#', '#', '#']
r = re.findall("[^\w]", "abcde ``  acccdd%%cea  $$ deabe1234+++###")  # 单词字符
print(r)  # [' ', '`', '`', ' ', ' ', '%', '%', ' ', ' ', '$', '$', ' ', '+', '+', '+', '#', '#', '#']

# 数量词用在字符或者[]之后
r = re.findall("abc*", "abcde ``  acccdd%%cea  $$ deabe1234+++###")  # *表示0个-n个
print(r)  # ['abc', 'ab']
r = re.findall("abc+", "abcde ``  acccdd%%cea  $$ deabe1234+++###")  # +表示1个-n个
print(r)  # ['abc']
r = re.findall("abc?", "abcde `abcc`  acccdd%%cea  $$ deabe1234+++###")  # ?表示0个-1个
print(r)  # ['abc', 'ab']
r = re.findall("ab{2}c", "abcde `abbcc`  acccdd%%cea  $$ deabe1234+++###")  # {m}表示前一个字符m次
print(r)  # ['abbc']

b = "chuan1zhi2"
print(re.sub("\d", "_", b))  # chuan_zhi_       替换
p = re.compile("\d")
r = p.findall("abcde `abbcc`  acccdd%%cea  $$ deabe1234+++###")
print(r)  # ['1', '2', '3', '4'] p带了正则表达式的re
print(p.sub("_", b))
p = re.compile(".")
r = p.findall("\n")
print(r)  # []
p = re.compile(".", re.S)
r = p.findall("\n")
print(r)  # ['\n']
a = "a\nb"
print(len(a))  # 3
print(a[1])  # '\n'
b = r"a\nb"
print(len(b))  # 4
print(b[1])  # '\\'
