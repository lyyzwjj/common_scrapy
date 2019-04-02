import re

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
r = re.findall("[\s]", "abcde   acccddcea   deabe1234")  # 非空白字符
print(r)  # [' ', ' ', ' ', ' ', ' ', ' ']
r = re.findall("[< >\t\r\n\f\v]", "abcde   acccddcea   deabe1234")  # 非空白字符
print(r)  # [' ', ' ', ' ', ' ', ' ', ' ']
