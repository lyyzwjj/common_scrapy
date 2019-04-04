# coding=utf-8
import requests
import re
import json


class Neihan:
    def __init__(self):
        # self.start_url = "https://ishuo.cn/"
        self.start_url = "http://www.chengyugushi.net/sizichengyu/list_1_1.html"
        self.next_url_temp = "http://www.chengyugushi.net/sizichengyu/list_1_{}.html"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_first_page_content_list(self, html_str):
        # re.findall(r"<p>(.*?)</p>", html_str, re.S)
        # content_list = re.findall(r"<div class=\"content\">(.*?)</div>", html_str, re.S)
        # 更精确匹配<li class="list_li"><div class="content">有位语文老师为学生朗诵了一首陆游的《卧春》，要求学生听写出来……</div><div class="info"><span class="right tags"><label class="tag"></label><a href="/member/4">笑话</a>,<a href="http://ishuo.cn/special/qiushibaike">糗事百科</a>,<a href="http://ishuo.cn/special/tingxie">听写</a></span><a href="/subject/5888">糗事百科之听写</a>04月29日0个评论 0人喜欢</div></li>
        # content_list = re.findall(r"<li class=\"list_li\">.*?<div class=\"content\">(.*?)</div>", html_str, re.S)
        # content_list = re.findall(r"<small>.*?</small>.*?<br />(.*?)</li>", html_str, re.S)
        content_list = re.findall(r"<small>.*?<br />(.*?)</li>", html_str, re.S)
        # content_list = re.findall(r"<small>.*?<br />(^[\t|\n|r]*?)</li>", html_str, re.S)
        print(content_list)
        print(len(content_list))
        return content_list

    def save_content_list(self, content_list):
        with open("neihan.txt", "a", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))  # 输出中文
                f.write("\n")
        print("保存成功")

    def run(self):
        # 1.start_url
        # 2.发送请求获取响应
        html_str = self.parse_url(self.start_url)
        # 3.提取数据
        content_list = self.get_first_page_content_list(html_str)
        # 4.保存
        self.save_content_list(content_list)
        i = 1
        while len(content_list) == 10:
            i += 1
            # 5.构造下一个的url地址
            next_url = self.next_url_temp.format(i)
            html_str = self.parse_url(next_url)
            content_list = self.get_first_page_content_list(html_str)
            self.save_content_list(content_list)


if __name__ == '__main__':
    nh = Neihan()
    nh.run()
