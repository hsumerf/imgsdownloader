# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from time import sleep

#facebook unfriender bot with scrapy+selenium
class FbSpider(scrapy.Spider):
    name = 'fb'
    allowed_domains = ['facebook.com']
    def start_requests(self):
        driver = webdriver.Chrome('/home/hsumerf/Desktop/chromedriver')
        driver.get('https://www.facebook.com')
        sleep(3)
        email = driver.find_element_by_name('email')
        email.send_keys('h.s.umer.farooq@gmail.com')
        password = driver.find_element_by_name('pass')
        password.send_keys('password')
        login = driver.find_elements_by_id('u_0_2')
        login[0].click()
        sleep(10)
        max_limit = 500
        count = 0
        total_10_multiples = 5
        while True:
            if max_limit>count:
                driver.get('https://m.facebook.com/friends/center/requests/outgoing')
                sleep(5)
                names = driver.find_elements_by_xpath('//*[@class="_52jh _5pxc"]')
                undos = driver.find_elements_by_xpath("//*[@class='_54k8 _52jh _56bs _56bt']")
                for i in range(len(undos)):
                    undos[i].click()
                    sleep(3)
                    count = count + 1
                    # writing name in file
                    unfriend_file_name = 'unfriend_file.txt'
                    unfriend_pointer = open(unfriend_file_name,'a')
                    unfriend_pointer.write(names[i].text)
                    unfriend_pointer.write("\n")
            else:
                unfriend_pointer.close()
                driver.close()
