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
cookies = "Cookie: _ga=GA1.2.1912297313.1552320847; _gid=GA1.2.434464513.1552320847; BAIDU_SSP_lcr=https://www.baidu.com/link?url=2c2Cq_igCmpp48ZXHtbtM7hDDj7pwaW2cSSd3-KiH3e&wd=&eqid=ef708c690007a51c000000065c86898f; Hm_lvt_76c941eab16e9b48cd0fb4a6d9482a4f=1552320846,1552320914; _gat=1; jqCP_887f_noticeTitle=1; jqCP_887f_saltkey=N18113dd; jqCP_887f_lastvisit=1552317322; jqCP_887f_sid=k4zQCz; jqCP_887f_lastact=1552320922%09index.php%09; Hm_lpvt_76c941eab16e9b48cd0fb4a6d9482a4f=1552320922"

# 字典推导式
cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split(";")}

print(cookies)

session.post(post_url, data=post_data, headers=headers)
r = session.get("http://www.renren.com/327550029/profile", headers=headers, cookies=cookies)
with open("renren.html", "w", encoding="utf-8") as f:
    f.write(r.content.decode())

cookies = {i: i + 10 for i in range(10)}
print(cookies)
