import scrapy
from scrapy.selector import Selector


class DHISpider(scrapy.Spider):
    name = "herbmedpro"
    start_urls = [
       'http://cms.herbalgram.org/herbmedpro/index.html#param.wapp?sw_ page =@@herblist%3Fletter%3DAll',
    ]  
    def parse(self, response):
        
        for href in response.xpath('').extract():
            yield response.follow(href, self.parse_name)
    
    def parse_name(self, response):
        for nccih in response.xpath(''):
            yield {
                #NIH-NCCIH
                'name_herbs': nccih.xpath('').extract(),
                'latin_name' :nccih.xpath('').extract(),
                'description': nccih.xpath('').extract(),
            }