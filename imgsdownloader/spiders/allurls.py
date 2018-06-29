# -*- coding: utf-8 -*-
import scrapy

class AllurlsSpider(scrapy.Spider):
    name = 'allurls'
    allowed_domains = ['smrafiq.com']
    start_urls = ['http://smrafiq.com']

    def start_requests(self):
        yield scrapy.Request('http://smrafiq.com', self.parse)


    def parse(self, response):

        print(response.url)
        new_path = 'urls.txt'
        new_days = open(new_path,'a')
        new_days.write(response.url)
        new_days.write("\n")


        for url in response.xpath('//a/@href').re('(?!.*#)^.*$'):

            yield scrapy.Request(url, callback=self.parse)

        new_days.close()
