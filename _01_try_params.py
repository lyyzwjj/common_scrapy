# coding=utf-8
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}
p = {"wd": "传智播客"}
url_temp = "https://www.baidu.com/s?"
# resp = requests.get(url_temp, headers=headers, params=p)
# print(resp.status_code)
# # print(resp.request.url)
# print(resp.content.decode())
# url = "https://www.baidu.com/s?wd=%s" % "传智播客"
url = "https://www.baidu.com/s?wd={}".format("传智播客")
resp = requests.get(url, headers=headers)
print(resp.status_code)
print(resp.request.url)
# cprint(resp.content.decode())

# 字符串格式化的另一种方式
url = "https://www.baidu.com/{}s?wd={},{}".format("传智播客", [1, 2, 3], {"a": "1"})
print(url)

