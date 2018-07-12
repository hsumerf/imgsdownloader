# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from time import sleep


class InstaLoginSpider(scrapy.Spider):
    name = 'insta_login'
    allowed_domains = ['instagram.com']
    def start_requests(self):
        driver = webdriver.Chrome('/home/hsumerf/Desktop/chromedriver')
        sleep(1)
        driver.get('https://www.instagram.com/accounts/login/')
        sleep(3)
        #page_source = driver.page_source
        username = driver.find_element_by_name('username')
        username.send_keys('h.s.umer.farooq@gmail.com')
        password = driver.find_element_by_name('password')
        password.send_keys('')
        login = driver.find_element_by_tag_name('button')
        login.click()
        sleep(5)
        driver.get('https://www.instagram.com/hsumerfarooq/')
            #extract following from pop window
        following = driver.find_elements_by_class_name('-nal3')[2]
        following.click()
        sleep(5)
        buttons = driver.find_elements_by_tag_name('button')
        unfollower_names = driver.find_elements_by_xpath("//*[@class='FPmhX notranslate zsYNt ']")
        unfollow_limit = 5
        unfollow_count = 0
        while number < unfollow_limit:

            for i in range(3,14):
                button = buttons[i]
                if button.text == "Following":
                    unfollower_name = unfollower_names[unfollow_count].text
                    unfollow_count = unfollow_count + 1
                    unfollower_file = 'unfollower_file.txt'
                    unfollowing_pointer = open(unfollower_file,'a')
                    unfollowing_pointer.write(unfollower_name)
                    unfollowing_pointer.write("\n")
                    button.click()
                    #         # to confirm
                    confirm = driver.find_element_by_xpath('//*[text()="Unfollow"]')
                    confirm.click()


        # #to unfollow
        # for button in buttons:
        #     if button.text == "Following":
        #         button.click()
        #         # to confirm
        #         confirm = driver.find_element_by_xpath('//*[text()="Unfollow"]')
        #         confirm.click()
        #     else:
        #         pass
        driver.close()



    # def parse(self, response):
    #     print(response.url)
    def parse(self, response):
        pass
