# -*- coding: utf-8 -*-
#images downloader code complete
# import scrapy
# from imgsdownloader.items import ImgsdownloaderItem
#
#
# class SmpicsSpider(scrapy.Spider):
#     name = 'smpics'
#     allowed_domains = ['smrafiq.com']
#     start_urls = ['http://smrafiq.com/']
#
#     def parse(self, response):
#         img_url = ImgsdownloaderItem()
#         for elem in response.xpath("//img"):
#
#             img_url = elem.xpath("@src").extract_first()
#             print(img_url)
#             yield {'image_url': [img_url]}
import scrapy
from imgsdownloader.items import ImgsdownloaderItem
import re
class SmpicsSpider(scrapy.Spider):
    name = 'smpics'
    allowed_domains = ['smrafiq.com']
    start_urls = ['http://smrafiq.com']

    # downloading images code complete
    def parse(self, response):
     #   item = ImgsdownloaderItem()  # init class
        for elem in response.xpath("//img"):
            img_url = elem.xpath("@src").extract_first()
            # img_url = re.findall(r"(?!.* )^.*$", img_url)[0]

            yield {'image_urls': [img_url]}