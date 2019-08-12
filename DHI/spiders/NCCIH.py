import scrapy
from scrapy.selector import Selector


class DHISpider(scrapy.Spider):
    name = "nccih"
    start_urls = [
       'https://nccih.nih.gov/health/herbsataglance.htm',
    ]  
    def parse(self, response):
        
        for href in response.xpath('body//div[@class="container"]//div[@class="main-container"]//div//section//div//section[@id="block-system-main"]//div//div//div//div[@class="panel-panel panel-col-top"]//div//div[@class="panel-pane pane-entity-field pane-node-body"]//div//div//div//div//div[@class="container-fluid"]//div//div//ul//li//a/@href').extract():
            yield response.follow(href, self.parse_name)
    
    def parse_name(self, response):
        for nccih in response.xpath('//body//div[@class="container"]//div[@class="main-container"]//div//section[@class="col-sm-12"]'):
            yield {
                #NIH-NCCIH
                'name_herbs': nccih.xpath('//h1/text()').extract(),
                'latin_name' :nccih.xpath('//div[@class="region region-content"]//section[@id="block-system-main"]//div//div[@class="row"]//div[@class="col-md-8 fsheetcontent"]//div//div//div//div//div[@class="field field-name-field-latin-name field-type-text field-label-inline clearfix"]//div[@class="field-items"]//div//em/text()').extract(),
                'description': nccih.xpath('//div[@class="region region-content"]//section[@id="block-system-main"]//div//div[@class="row"]//div[@class="col-md-8 fsheetcontent"]//div//div//div//div//div[@class="field field-name-body field-type-text-with-summary field-label-hidden clearfix"]//div//div//ul//li/text()').extract(),
            }