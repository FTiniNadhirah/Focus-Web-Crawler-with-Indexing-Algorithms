import scrapy
from scrapy.selector import Selector

class DHISpider(scrapy.Spider):
    name = "mhpdc"
    start_urls = [
        'http://www.globinmed.com/index.php?option=com_content&view=category&id=24&Itemid=144', 

    ]  
    def parse(self, response):
        for href in response.xpath('//body//div//div//div[@class="wrapper"]//div//div[@id="maincol"]//div//div[@id="maincontent-block"]//section//div//form//table//tbody//tr//td//a/@href').extract():
            yield response.follow(href, self.parse_name)

        next_page = response.xpath('//body//div//div//div[@class="wrapper"]//div//div[@id="maincol"]//div//div[@id="maincontent-block"]//section//div//form//div[@class="pagination"]//div//div[@class="tab"]//div[@class="tab2"]//strong//a/@href').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
            
    def parse_name(self, response):
        def extract_with_css(query):
            return response.xpath(query).extract()
        yield{
           'herbs_name' : extract_with_css('normalize-space(.//body//div//div//div[@class="wrapper"]//div[@class="alt"]//div[@id="maincol"]//div//div[@id="maincontent-block"]//div[@class="rt-article"]//div//div[@class="article-header"]//div[@class="main-article-title"]//h2/text())'),
           'description' : extract_with_css('//body//div//div//div[@class="wrapper"]//div[@class="alt"]//div[@id="maincol"]//div//div[@id="maincontent-block"]//div[@class="rt-article"]//div[@class="full-article"]//p/text()'),
        }