# -*- coding: utf-8 -*-
import scrapy


class AllextractSpider(scrapy.Spider):
    name = 'AllExtract'
    allowed_domains = ['smrafiq.com']
    start_urls = ['http://smrafiq.com/']

    def start_requests(self):
        yield scrapy.Request('http://smrafiq.com', self.parse)

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
    #   All urls in new file urls.txt
        print(response.url)
        urls_path = 'urls.txt'
        new_urls = open(urls_path,'a')
        new_urls.write(response.url)
        new_urls.write("\n")
#   extract all urls in Page
        for url in response.xpath('//a/@href').re('(?!.*#)^.*$'):
            yield scrapy.Request(url, callback=self.parse)
    #close file
        new_urls.close()