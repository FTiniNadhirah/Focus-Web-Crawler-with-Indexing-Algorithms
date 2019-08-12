import scrapy
from scrapy.selector import Selector


class DHISpider(scrapy.Spider):
    name = "mpid"
    start_urls = [
        'http://libproject.hkbu.edu.hk/was40/detail?lang=en&record=1&channelid=1288&searchword=alphabet%3DA',
        'http://libproject.hkbu.edu.hk/was40/detail?lang=en&record=2&channelid=1288&searchword=alphabet%3DA',
        '',
    ]  
    
    def parse(self, response):
        for nccih in response.xpath('//div//table//tbody//tr//td//table//tbody//tr//td[@class="text"]'):
            yield {
                #NIH-NCCIH
                'name_herbs': nccih.xpath('//table//tbody//tr//td[@class="text"]/text()').extract(),
                'descriptions' :nccih.xpath('//table//tbody//tr//td[@class="text"]/text()').extract(),
            }