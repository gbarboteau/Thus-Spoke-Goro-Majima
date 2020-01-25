import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://yakuza.fandom.com/wiki/Category:Playable_Characters']

    def parse(self, response):
        for title in response.css('div.category-page__member-left + a'):
            yield {'character': title.css('a ::text').get()}
