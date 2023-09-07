import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import json

class ReviewItem(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()

class CoolSpider(scrapy.Spider):
    name = 'docc'
    start_urls = ['https://2doc.by/doctor/kot-maksim-vladimirovich']

    def parse(self, response):
        rew = response.css('div.leading-7')
        for q in rew:
            item = ReviewItem()
            item['text'] = q.css('div.leading-7 p::text').get()
            #autt = q.css('div.md\\:leading-7::text').get()
            #item['author'] = q.css('div.md.leading-7::text').get().replace(",\n", "").split()[0]
            yield item

    
