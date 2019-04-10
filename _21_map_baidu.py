# coding=utf8
import requests
import json
import demjson
from openpyxl import Workbook


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

    def save_content_list(self, content_list):  # 保存数据
        if len(content_list) != 0:
            wb = Workbook()  # 创建文件对象
            # grab the active worksheet
            ws = wb.active  # 获取第一个sheet
            ws.append(list(content_list[0].keys()))
            for content in content_list:
                ws.append(list(content.values()))
            wb.save(self.city_name + self.kw + ".xlsx")
        else:
            print("暂未查到数据")
        print(content_list)

    def save_addr(self, item, content, name, content_name, *args):
        if content.get(content_name) is None:
            item[name] = {}
            for arg in args:
                item[name][arg] = content[arg]
            item[name] = json.dumps(item[name], ensure_ascii=False)
        else:
            item[name] = json.dumps(content[content_name], ensure_ascii=False)

    def run(self):
        pn = 0
        content_list = []
        while pn != -1:
            # 1.start_url
            # 2.发送请求,获取响应
            json_str = self.parse_url(self.url_temp.format(pn))
            # 3.提取数据,提取下一页的url地址
            # obj = json.loads(json_str)
            obj = demjson.decode(json_str, encoding="utf-8")
            if obj.get("content") is not None:
                for content in obj["content"]:
                    item = {}
                    item["name"] = json.dumps(content["name"], ensure_ascii=False)
                    # item["addr"] = content["address_norm"]
                    self.save_addr(item, content, "addr", "address_norm", "area_name", "addr")
                    item["x"] = json.dumps(content["x"], ensure_ascii=False)
                    item["y"] = json.dumps(content["y"], ensure_ascii=False)
                    try:
                        item["phone"] = json.dumps(content["ext"]["detail_info"]["phone"], ensure_ascii=False)
                    except KeyError:
                        item["phone"] = json.dumps(None, ensure_ascii=False)
                    content_list.append(item)
                pn += 1
            else:
                # 4.保存数据
                self.save_content_list(content_list)
                pn = -1


if __name__ == '__main__':
    map = BaiduMapSpider("太平人寿", "289")
    map.run()
