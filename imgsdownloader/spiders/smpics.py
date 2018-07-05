# -*- coding: utf-8 -*-
import scrapy
from imgsdownloader.items import ImgsdownloaderItem


class SmpicsSpider(scrapy.Spider):
    name = 'smpics'
    allowed_domains = ['smrafiq.com']
    start_urls = ['http://smrafiq.com/']

    def parse(self, response):
        img_url = ImgsdownloaderItem()
        for elem in response.xpath("//img"):

            img_url = elem.xpath("@src").extract_first()
            print(img_url)
            yield {'image_url': [img_url]}
