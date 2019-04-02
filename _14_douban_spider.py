# coding:utf-8
import requests
import json
import time


class DoubanSpider:
    def __init__(self):
        self.url_temp = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_american/items?os=ios&for_mobile=1&callback=jsonp1&start={}&count=18&loc_id=108288&_={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_list(self, json_str):
        dict_ret = json.loads(json_str)
        content_list = dict_ret[" "]
        total = dict_ret["count"]
        return content_list, total

    def save_content_list(self, content_list):
        with open("douban.txt", "a", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")

    def run(self):  # 实现主逻辑
        num = 0
        total = 100
        while num < total + 18:
            # 1. start_url
            t = time.time()
            url = self.url_temp.format(num, int(round(t * 1000)))
            # 2. 发送请求,获取响应
            json_str = self.parse_url(url)
            # 3. 提取出数据
            content_list, total = self.get_content_list(json_str)
            # 4. 保存
            self.save_content_list(content_list)
            # if len(content_list) < 18:
            #     break
            # 5. 构造下一页url地址,进入循环
            num += 18


if __name__ == '__main__':
    ds = DoubanSpider()
    ds.run()
