# coding:utf-8

import requests

# 发送请求
response = requests.get("https://www.baidu.com/img/bd_logo1.png")
#
# with open("a.png","w") as f:    w表示写字符串
with open("a.png", "wb") as f:  # wb表示写二进制内容
    f.write(response.content)

response = requests.get("https://www.sina.com.cn/")
with open("sina_content.html", "w") as f:
    f.write(response.content.decode())

response = requests.get("https://www.sina.com.cn/")
with open("sina_text.html", "w") as f:
    f.write(response.text)

post_url = "https://imac.hk/wp-login.php"
