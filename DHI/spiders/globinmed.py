import scrapy
from scrapy.selector import Selector


class DHISpider(scrapy.Spider):
    name = "globinmed"
    start_urls = [
       'http://www.globinmed.com/index.php?option=com_content&view=category&id=24&Itemid=144',
    ]  

    def parse(self, response):
        for href in response.xpath('//section[@class="category-list"]//div[@class="cat-items"]//table/tbody/tr//a/@href').extract():
            yield response.follow(href, self.parse_name)
    
        next_page = response.xpath('//section[@class="category-list"]//div[@class="cat-items"]//div[@class="pagination"]//div[@class="tab"]//div[@class="tab2"]//a/@href').extract()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_name(self, response):
        def extract_with_css(query):
            return response.xpath(query).extract()

        yield {
            'common_name': extract_with_css('normalize-space(.//div[@class="rt-article"]//div[@class="full-article"]//div[@class="article-header"]//h2[@class="contentheading"]/text())'), 
            'summary': extract_with_css('normalize-space(.//div[@class="rt-article"]//div[@class="full-article"]//p/text())'),
            'reference_texts': extract_with_css('normalize-space(.//div[@class="rt-article"]//div[@class="full-article"]//ol//li/text())'),
            'reference_links': extract_with_css('normalize-space(.//div[@class="rt-article"]//div[@class="full-article"]//ol//li//a/@href)'),
        }
