# -*- coding: utf-8 -*-
import scrapy
counter = 0

class AllurlsSpider(scrapy.Spider):
    name = 'allurls'
    allowed_domains = ['smrafiq.com']
    start_urls = ['http://smrafiq.com']

    def start_requests(self):
        yield scrapy.Request('http://smrafiq.com', self.parse)


    def parse(self, response):

        print(response.url,counter)
        for url in response.xpath('//a/@href').re('(?!.*#)^.*$'):
            print(url)
            yield scrapy.Request(url, callback=self.parse)
