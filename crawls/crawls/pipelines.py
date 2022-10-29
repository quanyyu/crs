# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from crawls.domain import ChapterDTO
import redis


class CrawlsPipeline:
    def process_item(self, item, spider):
        return item


class ChapterSavePipeline:

    def open_spider(self, spider):
        self.redis = redis.Redis()

    def close_spider(self, spider):
        self.redis.close()

    def process_item(self, item, spider):
        print("zadd...")
        self.redis.zadd(item.book_url, {item.content: item.index})