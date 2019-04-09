# coding=utf8
import requests
import json
import threading
import time
from lxml import html
from queue import Queue

etree = html.etree


class QuibaiSpider:
    def __init__(self):
        self.url_temp = "https://www.qiushibaike.com/hot/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
        # self.session = requests.session()
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_queue = Queue()

    def get_url_list(self):
        # return [self.url_temp.format(i) for i in range(1, 14)]
        for i in range(1, 14):
            self.url_queue.put(self.url_temp.format(i))

    def parse_url(self):
        while True:
            url = self.url_queue.get()
            print(url)
            response = requests.get(url, headers=self.headers)
            # response = self.session.get(url, headers=self.headers)
            # response = requests.get(url, headers=self.headers,cookies=cookies)
            # return response.content
            # return response.content.decode()
            self.html_queue.put(response.content.decode())
            self.html_queue.task_done()

    def get_content_list(self):
        while True:
            html_str = self.html_queue.get()
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
            self.content_queue.put(content_list)
            self.content_queue.task_done()

    def save_content_list(self):  # 保存数据
        while True:
            content_list = self.content_queue.get()
            file_path = "qiubai.txt"
            with open(file_path, "a", encoding="utf-8") as f:
                for content in content_list:
                    f.write(json.dumps(content, ensure_ascii=False, indent=2))
                    f.write("\n")
            self.content_queue.task_done()
        print("保存成功")

    def run(self):
        thread_list = []
        # 1.url_list
        # url_list = self.get_url_list()
        t_url = threading.Thread(target=self.get_url_list)
        thread_list.append(t_url)
        # 2.遍历发送请求
        # for url in url_list:
        # html_str = self.parse_url(url)
        for i in range(20):  # 多开几个线程
            t_parse = threading.Thread(target=self.parse_url)
            thread_list.append(t_parse)
        # 3.提取数据
        # content_list = self.get_content_list(html_str)
        for i in range(2):  # 开两个线程
            t_html = threading.Thread(target=self.get_content_list)
            thread_list.append(t_html)
        # 4,保存
        # self.save_content_list(content_list)
        t_save = threading.Thread(target=self.save_content_list)
        thread_list.append(t_save)
        for t in thread_list:
            t.setDaemon(True)  # 把子线程设置成守护线程,该线程不重要主线程结束,子线程结束
            t.start()

        for q in [self.url_queue, self.html_queue, self.content_queue]:
            q.join()  # 让主线程等待阻塞,等待队列的任务完成之后在完成
        print("主线程结束")


if __name__ == '__main__':
    t1 = int(round(time.time() * 1000))
    qiubai = QuibaiSpider()
    qiubai.run()
    t2 = int(round(time.time() * 1000))
    print("总耗时%s" % (t2 - t1))
