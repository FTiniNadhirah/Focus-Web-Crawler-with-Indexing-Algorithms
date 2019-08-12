import scrapy
from scrapy.selector import Selector


class DHISpider(scrapy.Spider):
    name = "med-nccih"
    start_urls = [
       'https://medlineplus.gov/druginfo/herb_All.html',
    ]  
    def parse(self, response):
        
        for href in response.xpath('//div[@class="section-body"]//ul//li//a/@href').extract():
            yield response.follow(href, self.parse_name)
    
    def parse_name(self, response):
        for nccih in response.xpath('//body//div[@class="container"]//div[@class="main-container"]//div//section[@class="col-sm-12"]'):
            yield {
                #NIH-NCCIH
                'name_herbs': nccih.xpath('//h1/text()').extract(),
                'latin_name' :nccih.xpath('//div[@class="region region-content"]//section[@id="block-system-main"]//div//div[@class="row"]//div[@class="col-md-8 fsheetcontent"]//div//div//div//div//div[@class="field field-name-field-latin-name field-type-text field-label-inline clearfix"]//div[@class="field-items"]//div//em/text()').extract(),
                'description': nccih.xpath('//div[@class="region region-content"]//section[@id="block-system-main"]//div//div[@class="row"]//div[@class="col-md-8 fsheetcontent"]//div//div//div//div//div[@class="field field-name-body field-type-text-with-summary field-label-hidden clearfix"]//div//div//ul//li/text()').extract(),
            }