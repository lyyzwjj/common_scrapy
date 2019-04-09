# coding=utf8
import requests
import json
from lxml import html

etree = html.etree


class QuibaiSpider:
    def __init__(self):
        self.url_temp = "https://www.qiushibaike.com/hot/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
        self.session = requests.session()

    def get_url_list(self):
        return [self.url_temp.format(i) for i in range(1, 14)]

    def parse_url(self, url):
        print(url)
        # response = requests.get(url, headers=self.headers)
        response = self.session.get(url, headers=self.headers)
        # response = requests.get(url, headers=self.headers,cookies=cookies)
        return response.content.decode()
        # return response.content

    def get_content_list(self, html_str):
        html = etree.HTML(html_str)
        div_list = html.xpath('//div[@id="content-left"]/div')  # 根据div分组
        content_list = []
        for div in div_list:
            item = {}
            item["content"] = div.xpath(".//div[@class='content']/span/text()")
            item["content"] = [i.replace("\n", "") for i in item["content"]]
            item["author_gender"] = div.xpath(".//div[contains(@class,'articleGender')]/@class")
            item["author_gender"] = item["author_gender"][0] if len(item["author_gender"]) > 0 else None
            item["author_age"] = div.xpath(".//div[contains(@class,'articleGender')]/text()")
            item["author_age"] = item["author_age"][0] if len(item["author_age"]) > 0 else None
            item["content_img"] = div.xpath(".//div[@class='thumb']/a/img/@src")
            item["content_img"] = "https:" + item["content_img"][0] if len(item["content_img"]) > 0 else None
            item["author_img"] = div.xpath(".//div[@class='author clearfix']//img/@src")
            item["author_img"] = "https:" + item["author_img"][0] if len(item["author_img"]) > 0 else None
            item["stats_vote"] = div.xpath(".//span[@class='stats-vote']/i/text()")
            item["stats_vote"] = item["stats_vote"][0] if len(item["stats_vote"]) > 0 else None
            content_list.append(item)
        return content_list

    def save_content_list(self, content_list):  # 保存数据
        file_path = "qiubai.txt"
        with open(file_path, "a", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False, indent=2))
                f.write("\n")
        print("保存成功")

    def run(self):
        # 1.url_list
        url_list = self.get_url_list()
        # 2.遍历发送请求
        for url in url_list:
            html_str = self.parse_url(url)
            # with open("qiubai_learn.html", "w", encoding="utf-8") as f:
            #     f.write(html_str)
            # 3.提取数据
            content_list = self.get_content_list(html_str)
            # 4,保存
            self.save_content_list(content_list)


if __name__ == '__main__':
    qiubai = QuibaiSpider()
    qiubai.run()
