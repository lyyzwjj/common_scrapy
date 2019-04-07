# coding=utf-8
from lxml import html
import re

etree = html.etree
with open("lxml_learn.html", "r", encoding="utf-8") as f:
    text = f.read()
html = etree.HTML(text)
# print(html)
# 查看element对象中包含的字符串
print(etree.tostring(html).decode())

ret1 = html.xpath('//div[@class="pl2"]/a/@href')
ret2 = html.xpath('//div[@class="pl2"]/a/text()[1]')
print(ret1)
print(ret2)
# url 和文本组成一个字典
for href in ret1:
    item = {}
    item["href"] = href
    item["title"] = ret2[ret1.index(href)].rstrip("/ ").strip()
    print(item)

print("*" * 100)
# 分组,根据div标签进行分组,对每一组继续写xpath
ret3 = html.xpath('//div[@class="pl2"]')
for i in ret3:
    item = {}
    item["title"] = i.xpath("./a/text()")[0].rstrip("/ ").strip() if len(i.xpath("./a/text()")) else None
    item["href"] = i.xpath("./a/@href")[0] if len(i.xpath("./a/@href")) else None
    print(item)
