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
