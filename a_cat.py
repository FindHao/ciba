import requests
from bs4 import BeautifulSoup
import bs4
import re
from word import Word

voice_url_reg = re.compile("(http.*)'")


class Query:
    def __init__(self):
        self.s = requests.session()
        self.s.headers.update({
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch", "Accept-Language": "en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4",
            "Cache-Control": "max-age=0",
        })
        self.word = Word()

    def get(self, word_str):
        self.word = Word()
        r = self.s.get("http://www.iciba.com/%s" % word_str)
        soup = BeautifulSoup(r.content, "lxml")
        # todo: 如果没有搜索结果，需要更新
        temp_results = soup.find_all("div", class_="in-base")

        if not temp_results:
            return True
        # 获取发音和音标
        base = temp_results[0]

        temp_results = base.find_all("div", class_="in-base-top")
        if temp_results:
            if temp_results[0].div.get('style'):
                self.word.props[''] = temp_results[0].div.text
                return True

        # with open("test", 'w') as fout:
        #     fout.write(base.prettify())
        # todo: 只有一个发音的那种会出错 fra
        temp_results = base.find_all("div", class_="base-speak")
        if temp_results:
            temp = temp_results[0]
            for node in temp:
                temp1 = ''
                temp2 = ''
                if isinstance(node, bs4.element.Tag):
                    for node1 in node:
                        if not isinstance(node1, bs4.element.Tag):
                            continue
                        if node1.name == 'span':
                            temp1 = node1.text
                        elif node1.name == 'i':
                            temp3 = voice_url_reg.findall(node1['ms-on-mouseover'])
                            if temp3:
                                temp2 = temp3[0]

                    self.word.voices.append((temp1, temp2))
        # 获取基本词义
        temp_results = base.find_all('ul', class_='base-list')
        # print(temp_results)
        if temp_results:
            temp = temp_results[0]
            for node in temp:
                if isinstance(node, bs4.element.Tag):
                    temp_prop = node.span.text
                    temp_str = ''
                    for x in node.p:
                        if isinstance(x, bs4.element.Tag):
                            temp_str += x.text
                    self.word.props[temp_prop] = temp_str
