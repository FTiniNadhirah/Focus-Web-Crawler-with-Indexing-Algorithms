import scrapy
from scrapy.selector import Selector


class DHISpider(scrapy.Spider):
    name = "med-ods"
    start_urls = [
       'https://medlineplus.gov/druginfo/herb_All.html',
    ]  

    def parse(self, response):
        for href in response.xpath('//div[@class="section-body"]//ul//li//a/@href').extract():
            yield response.follow(href, self.parse_name)

    def parse_name(self, response):
        for ods in response.xpath('//body//form//div[@id="container"]//div[@id="maincontent"]//div[@id="main"]'):
            yield {
                #NIH-ODS
                'name_herbs': ods.xpath('//div[@id="fstitle"]//div[@id="fstitleborder"]//h1/text()').extract(),  
                'descriptions': ods.xpath('//div[@class="center"]//p/text()').extract(),  
            }