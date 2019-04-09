# coding=utf8
import requests
import json
import demjson


class BaiduMapSpider:
    def __init__(self, kw, city_name):
        self.kw = kw
        self.city_name = city_name
        self.url_temp = "https://map.baidu.com/?&qt=s&wd=" + self.kw + "&c=" + self.city_name + "&pn={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}

    def parse_url(self, url):
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def save_content_list(self, obj):  # 保存数据
        print(obj)

    def run(self):
        pn = 0
        content_list = []
        while pn != -1:
            # 1.start_url
            # 2.发送请求,获取响应
            json_str = self.parse_url(self.url_temp.format(pn))
            # 3.提取数据,提取下一页的url地址
            # obj = json.loads(json_str)
            print(json_str)
            obj = demjson.decode(json_str, encoding="utf-8")
            if (obj.get("content") is None):
                pn = -1
                return
            for content in obj["content"]:
                item = {}
                item["name"] = content["name"]
                item["addr"] = content["address_norm"]
                item["navi_x"] = content["navi_x"]
                item["navi_y"] = content["navi_y"]
                item["phone"] = content["ext"]["detail_info"]["phone"]
                content_list.append(item)
            # 4.保存数据
            self.save_content_list(content_list)
            pn += 1


if __name__ == '__main__':
    map = BaiduMapSpider("太平", "289")
    map.run()
