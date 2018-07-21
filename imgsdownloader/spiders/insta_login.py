# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from time import sleep

#auto insta unfollower bot from scrapy+selenium
class InstaLoginSpider(scrapy.Spider):
    name = 'insta_login'
    allowed_domains = ['instagram.com']
    def start_requests(self):
        driver = webdriver.Chrome('/home/hsumerf/Desktop/chromedriver')
        sleep(1)
        driver.get('https://www.instagram.com/accounts/login/')
        sleep(2)
        #page_source = driver.page_source
        username = driver.find_element_by_name('username')
        username.send_keys('h.s.umer.farooq@gmail.com')
        password = driver.find_element_by_name('password')
        password.send_keys('password')
        login = driver.find_element_by_tag_name('button')
        login.click()
        sleep(2)
        total_unfollower = 0
        unfollow_limit = 49
        while True:
            unfollow_count = 0
            driver.get('https://www.instagram.com/hsumerfarooq/')
            sleep(3)
                #extract following from pop window
            following = driver.find_elements_by_class_name('-nal3')[2]
            following.click()
            sleep(3)
            buttons = driver.find_elements_by_tag_name('button')
            unfollower_names = driver.find_elements_by_xpath("//*[@class='FPmhX notranslate zsYNt ']")
            sleep(5)
            for i in range(len(buttons)):
                print(i)
                button = buttons[i]
                #because button.text could have Options instead of Following
                if button.text == "Following":
                    if unfollow_limit>total_unfollower:

                    #writing the name of follower
                        unfollower_name = unfollower_names[unfollow_count].text
                        unfollow_count = unfollow_count + 1
                        unfollower_file = 'unfollower_file.txt'
                        unfollowing_pointer = open(unfollower_file,'a')
                        unfollowing_pointer.write(unfollower_name)
                        unfollowing_pointer.write("\n")
                        #unfollow click
                        button.click()
                        sleep(3)
                        #         # to confirm
                        confirm = driver.find_element_by_xpath('//*[text()="Unfollow"]')
                        confirm.click()
                        sleep(3)
                        total_unfollower = total_unfollower+1
                        sleep(3)
                        #if limit exceded than break the program
                    else:
                        driver.close()
                else:
                    pass


        # #to unfollow
        # for button in buttons:
        #     if button.text == "Following":
        #         button.click()
        #         # to confirm
        #         confirm = driver.find_element_by_xpath('//*[text()="Unfollow"]')
        #         confirm.click()
        #     else:
        #         pass
        unfollowing_pointer.close()
        driver.close()



    # def parse(self, response):
    #     print(response.url)
    def parse(self, response):
        pass
