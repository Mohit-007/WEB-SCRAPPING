import scrapy
from ..items import WebScrapperItem

'''
class QuoteSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["http://quotes.toscrape.com/"]
    
    def parse(self, response):
       text = response.css('span.text::text')[0].extract()
       yield {'titletext': text}
#       title = response.css('title').extract()
#       title = response.css('title::text').extract()
#       yield {'titletext': title}
'''

'''

class QuoteSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["http://quotes.toscrape.com/"]
    
    def parse(self, response):
       text = response.css('span.text::text')[0].extract()
       yield {'titletext': text}
#       title = response.css('title').extract()
#       title = response.css('title::text').extract()
#       yield {'titletext': title}

'''

'''

class QuoteSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["http://quotes.toscrape.com/"]
    
    def parse(self, response):
        all_div_quotes = response.css('div.quote')[0]
        title = all_div_quotes.css('span.text::text').extract()
        author = all_div_quotes.css('.author::text').extract()
        tag = all_div_quotes.css('.tag::text').extract()
        yield {'title' : title,'author' : author,'tag' : tag }

'''

class QuoteSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["http://quotes.toscrape.com/"]
    
    def parse(self, response):
        
        items = WebScrapperItem()
        
        all_div_quotes = response.css('div.quote')
        
        for quotes in all_div_quotes:        
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()
            
            items['title'] = title
            items['author'] = author
            items['tag'] = tag
            yield items           
#            yield {'title' : title,'author' : author,'tag' : tag }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)    
            