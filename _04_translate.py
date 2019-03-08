# coding=utf8
import requests
import json
import sys

print(sys.argv)
query_string = sys.argv[1]

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}

"""
from: zh
to: en
query: 你好,朋友
transtype: enter
simple_means_flag: 3
sign: 863271.642838
token: 37ddb671333253d6a4584b5bf9568d8b
"""
data = {
    "form": "zh",
    "to": "en",
    # "query": "你好,朋友",
    "query": query_string,
    "source": "txt"
}
post_url = "https://fanyi.baidu.com/transapi"
r = requests.post(post_url, data=data, headers=headers)

if __name__ == '__main__':
    print(r.content.decode())
    dict_ret = json.loads(r.content.decode())
    ret = dict_ret["data"][0]["dst"]
    print("result is :", ret)
