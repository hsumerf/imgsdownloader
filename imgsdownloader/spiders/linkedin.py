# -*- coding: utf-8 -*-
import scrapy
    from selenium import webdriver
from time import sleep
class LinkedinSpider(scrapy.Spider):
    name = 'linkedin'
    allowed_domains = ['linkedin.com']
    def start_requests(self):
        driver = webdriver.Chrome('/home/hsumerf/Desktop/chromedriver')
        driver.get('https://www.linkedin.com')
        sleep(3)
        #page_source = driver.page_source
        email = driver.find_element_by_class_name('login-email')
        email.send_keys('h.s.umer.farooq@gmail.com')
        password = driver.find_element_by_class_name('login-password')
        password.send_keys('cscourse+-789')
        submit = driver.find_element_by_xpath('//*[@type="submit"]')
        submit.click()



    # def parse(self, response):
    #     print(response.url)
