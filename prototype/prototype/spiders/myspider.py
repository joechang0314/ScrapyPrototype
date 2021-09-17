import scrapy
from prototype.items import PrototypeItem

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.zyte.com/blog/']
    

    def parse(self, response):

        base_url = 'https://www.zyte.com'
        for title in response.css('.oxy-post-title'):
            item = PrototypeItem()
            item['title'] = title.css('::text').get()
            item['url'] = base_url + title.attrib['href']
            yield item

        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)
