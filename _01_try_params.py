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
# dict 和 cookiejar转换
c = requests.utils.dict_from_cookiejar(resp.cookies)
# c {'BAIDUID': '8B14268E1921F7317266B39043486715:FG=1', 'BIDUPSID': '8B14268E1921F7317266B39043486715', 'H_PS_PSSID': '1433_21120_28557_28608_28585_28640_26350_28603_28626_28605', 'PSINO': '1', 'PSTM': '1552499625', 'delPer': '0', 'BDSVRTM': '12', 'BD_CK_SAM': '1'}
requests.utils.cookiejar_from_dict(c)
# url地址的解码
requests.utils.unquote("https%3a%2f%2fwww.baidu.com%2f")
requests.utils.quote("https://www.baidu.com/")
requests.get("https://www.baidu.com/", varify=False)
resp = requests.get("https://www.baidu.com/", timeout=10)
assert resp.status_code == 200
