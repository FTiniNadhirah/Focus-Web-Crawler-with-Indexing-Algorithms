import scrapy
from scrapy.selector import Selector

class DHISpider(scrapy.Spider):
    name = "amh"
    start_urls = [
       'https://botanical.com/botanical/mgmh/poison.html',
    ]  

    def parse(self, response):
        
        for href in response.xpath('//body//center//table//tr//td//a/@href').extract():
            yield response.follow(href, self.parse_name)
    
    def parse_name(self, response):
        def extract_with_css(query):
            return response.xpath(query).extract()

        yield {
            #MEDLINEPLUS
            'name_herbs': extract_with_css('normalize-space(.//h1/text())'), 
            'descriptions': extract_with_css('//td/text()'),
            'drug_interaction': extract_with_css('//p/text()'),
            'latin_names': extract_with_css('normalize-space(.//h4/text())'), 
        }