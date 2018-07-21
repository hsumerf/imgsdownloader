# -*- coding: utf-8 -*-
import scrapy

#emails and numbers extractor from E-commerce websites
class RafiqindexSpider(scrapy.Spider):
    name = 'rafiqIndex'
    allowed_domains = ['smrafiq.com']
    start_urls = ['http://smrafiq.com/contact']

    def parse(self, response):

        emails_path = 'emails.txt'
        new_emails = open(emails_path,'a')
        #All emails in specific page
        #print(response.xpath('//*/text()').re('^.*@.*\.com'))
        for email in response.xpath('//*/text()').re('^.*@.*\.com'):
            new_emails.write(email)
            new_emails.write("\n")
        new_emails.close()

        #All Pak-Numbers
        #wrong re - >print(response.xpath('//*/text()').re('^\+92[\d- ]*$'))
        #print(response.xpath('//*/text()').re('^\+92[\d -]*$'))
        nums_path = 'nums.txt'
        new_nums = open(nums_path,'a')
        for num in response.xpath('//*/text()').re('^\+92[\d -]*$'):
            new_nums.write(num)
            new_nums.write("\n")
        new_nums.close()