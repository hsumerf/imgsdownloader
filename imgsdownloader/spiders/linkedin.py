# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver

class LinkedinSpider(scrapy.Spider):
    name = 'linkedin'
    allowed_domains = ['linkedin.com']
    def start_requests(self):
        driver = webdriver.Chrome('/home/hsumerf/Desktop/chromedriver')
        driver.get('https://www.linkedin.com')



    # def parse(self, response):
    #     print(response.url)
