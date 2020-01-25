import scrapy
from scrapy.selector import Selector

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.goodreads.com/author/quotes/1938.Friedrich_Nietzsche?page=1']

    def parse(self, response):
        for title in response.css('div.quoteText'):
            yield {'quote': title.css('div ::text').extract_first()}

            for next_page in response.css('a.next_page'):
                yield response.follow(next_page, self.parse)
