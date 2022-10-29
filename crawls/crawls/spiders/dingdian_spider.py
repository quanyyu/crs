import scrapy
import json
from lxml import etree
import json
from random_user_agent.user_agent import UserAgent

from crawls.domain import ChapterDTO


class DingdianSpider(scrapy.Spider):

    name = "dingdian_xiaoshuo"
    host = 'https://www.ddyueshu.com'
    user_agent = None

    def start_requests(self):
        urls = ['https://www.ddyueshu.com/4_4440/']
        ua_gen = UserAgent()
        self.user_agent = ua_gen.get_random_user_agent()

        for url in urls:
            yield scrapy.Request(url = url, 
            headers={"User-Agent": self.user_agent},
            callback=self.parse_chapter_list)

    def parse_chapter_list(self, response):
        file_name = 'test.html'
        with open(file_name, "wb") as f:
            f.write(response.body.decode("gbk").encode("utf-8"))
        root = etree.HTML(response.body)
        chapter_list = root.xpath("//div[@id='list']/dl")[0].getchildren()
        clear_chp_list = []
        start = False
        for ele in chapter_list:
            if ele.xpath("string(.)").find("正文") > 0:
                start = True
            elif start:
                clear_chp_list.append(ele)
        
        url_list = []
        for chp in clear_chp_list:
            url_list.append(self.host + chp.xpath("./a/@href")[0])

        self.logger.debug(f"find {url_list}")
        self.logger.info(f"find {len(url_list)} chapters")

        for idx,ch in enumerate(url_list):
            yield scrapy.Request(url=ch,
                        headers={"User-Agent": self.user_agent},
                        callback=self.parse_chapter_content, cb_kwargs={"index": idx, "book_url": response.url}
            )

    def parse_chapter_content(self, response, index, book_url):
        response._encoding = 'utf-8'
        dto = ChapterDTO()
        dto.index = index
        dto.name = response.xpath("//div[@class='bookname']/h1")[0].xpath('string(.)').get()

        content = response.xpath("//div[@id='content']")[0].xpath('string(.)').get()
        content = dto.name + "\n\n" + content
        content = content.replace('\xa0', '')
        content = content.replace("\r", "\n")
        content = content.replace("chaptererror();", "")
        content = content.replace("请记住本书首发域名：ddyueshu.com。顶点小说手机版阅读网址：m.ddyueshu.com", "")

        dto.content = content
        dto.url = response.url
        dto.book_url = book_url
        yield dto