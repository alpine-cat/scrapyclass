# -*- coding: utf-8 -*-
import scrapy
import test_proj.items as items
from scrapy_redis.spiders import RedisSpider


class HabrSpider(scrapy.Spider):
    name = 'habr'
    allowed_domains = ['habr.com']
    start_urls = ['http://habr.com/']

    def parse(self, response):
        article_urls = response.xpath("//li/article/h2[contains(@class, 'post__title')]/a/@href").extract()
        for x in article_urls:
            yield scrapy.Request(url=x, callback=self.call_parse)

    def call_parse(self, response):
        item = items.TestProjItem()
        item["name"] = response.xpath("//div[contains(@class, 'post__wrapper')]/h1/span/text()").extract_first()
        item["url"] = response.url
        item["body"] = response.xpath("//article/div[contains(@class, 'post__wrapper')]/div/div[@id='post-content-body']//text()").extract()
        return item


#make_request_from_data - in hw



