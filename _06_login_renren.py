# coding=utf8
import requests
import json
import sys

session = requests.session()

post_url = "http://www.renren.com/PLogin.do"
post_data = {
    "email": "mr_mao_hacker@163.com",
    "password": "alarmchime",
    "Cookie": ""
}
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
cookies = {

}
session.post(post_url, data=post_data, headers=headers)
r = session.get("http://www.renren.com/327550029/profile", headers=headers, cookies=cookies)
with open("renren.html", "w", encoding="utf-8") as f:
    f.write(r.content.decode())

# post_data = {
#     "formhash": "c28da74",
#     "referer": "http%3A%2F%2Fi.pcbeta.com%2Fspace-uid-4850111.html",
#     "username": "%CD%E8%DF%B9%D6%A5%CA%BF%CC%F5",
#     "password": "1e469fba64d208b7121d3ad130ccac9b",
#     "questionid": "0",
#     "answer": "",
#     "cookietime": "2592000"
# }
"""
formhash=0c28da74
&referer=http%3A%2F%2Fi.pcbeta.com%2Fspace-uid-4850111.html
&username=%CD%E8%DF%B9%D6%A5%CA%BF%CC%F5
&password=1e469fba64d208b7121d3ad130ccac9b
&questionid=0
&answer=
&cookietime=2592000
"""
