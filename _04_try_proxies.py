# coding=utf8
import requests
import json
import sys

proxies = {
    "http": "http://112.117.47.225:47120"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}

r = requests.get("http://www.baidu.com", proxies=proxies, headers=headers)

if __name__ == '__main__':
    print(r.status_code)
    print(r.content.decode())
