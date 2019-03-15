# coding:utf-8

import requests

post_url = "https://imac.hk/wp-login.php"

post_data = {
    "log": "wzzst310@163.com",
    "password": "Zzzst2017",
}
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}

response = requests.post(post_url, data=post_data, headers=headers)
print(response.content.decode())
