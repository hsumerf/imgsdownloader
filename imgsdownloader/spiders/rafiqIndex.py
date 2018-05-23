# -*- coding: utf-8 -*-
import scrapy


class RafiqindexSpider(scrapy.Spider):
    name = 'rafiqIndex'
    allowed_domains = ['smrafiq.com']
    start_urls = ['http://smrafiq.com/contact']

    def parse(self, response):
        #All emails in specific page
        print(response.xpath('//*/text()').re('^.*@.*\.com'))