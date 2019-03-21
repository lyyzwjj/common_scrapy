# coding:utf-8
import requests


class DoubanSpider:
    def __init__(self):
        self.start_url = ""
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def run(self):  # 实现主逻辑
        # 1. start_url
        # 2. 发送请求,获取响应
        # 3. 提取出数据
        # 4. 保存
        # 5. 构造下一页url地址,进入循环
        pass
