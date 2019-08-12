import scrapy
from scrapy.selector import Selector

class DHISpider(scrapy.Spider):
    name = "chmd"
    start_urls = [
        'http://herbaltcm.sn.polyu.edu.hk/herbal/search?type=-1&keyword=&page=1&item=50',
        'http://herbaltcm.sn.polyu.edu.hk/herbal/search?page=2&type=-1&keyword=&item=50',
        'http://herbaltcm.sn.polyu.edu.hk/herbal/search?page=3&type=-1&keyword=&item=50',
        'http://herbaltcm.sn.polyu.edu.hk/herbal/search?page=4&type=-1&keyword=&item=50',
        'http://herbaltcm.sn.polyu.edu.hk/herbal/search?page=5&type=-1&keyword=&item=50',
        'http://herbaltcm.sn.polyu.edu.hk/herbal/search?page=6&type=-1&keyword=&item=50',
        'http://herbaltcm.sn.polyu.edu.hk/herbal/search?page=7&type=-1&keyword=&item=50',
        'http://herbaltcm.sn.polyu.edu.hk/herbal/search?page=8&type=-1&keyword=&item=50',
        'http://herbaltcm.sn.polyu.edu.hk/herbal/search?page=9&type=-1&keyword=&item=50',
    ]  
    def parse(self, response):
        for href in response.xpath('//body//div//div[@class="content"]//div[@class="search-result"]//div//div[@class="result-list"]//div[@class="result-item"]//div[@class="left-part"]//div//div//a/@href').extract():
            yield response.follow(href, self.parse_name)

        # for next_page in response.xpath('//body//div//div[class="content"]//div[@class="search-result"]//div//div[@class="pagination-cont"]//div//form//a/@href').extract():
        #     yield response.follow(next_page, callback=self.parse)
            
    def parse_name(self, response):
        def extract_with_css(query):
            return response.xpath(query).extract()
        yield{
           'herbs_name' : extract_with_css('//body//div//div//div[@class="basic-info"]//div//div//div//div//div[@class="name"]//div[@class="eng-lat"]//dl//dd/text()'),
           'drug_interaction' : extract_with_css('//body//div//div//div[@class="other-info"]//div//div//div//div[@class="accordion"]//div[@class="accord-content"]//div//text()'),
        }