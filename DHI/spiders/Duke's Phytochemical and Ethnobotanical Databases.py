import scrapy
from scrapy.selector import Selector

class DHISpider(scrapy.Spider):
    name = "aa"
    start_urls = [
        'https://phytochem.nal.usda.gov/phytochem/search', 
    ]  
    def parse(self, response):
        for href in response.xpath('div.list-left div table tr td a::attr(href)').extract():
            yield response.follow(href, self.parse_name)

        next_page = response.css('div.list-left div.pagination a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
            
    def parse_name(self, response):
        herbs_name = response.css('div h2 span::text').extract()
        document = response.css('div ol li div div div div div.col-md-4 h5 a::attr(href)').extract()

        for item in zip(herbs_name,document):
            scraped_info = {
                'herbs_name' : item[0],
                'document' : [(item[1])], #Set's the url for scrapy to download images
        }
        yield scraped_info