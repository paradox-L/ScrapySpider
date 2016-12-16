from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider,Rule
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor

from douban_book_spider.items import DoubanBookSpiderItem

class DoubanBookSpider(CrawlSpider):
    name="douban_top_book_spider"
    download_delay=2
    allowed_domains=[]

    start_urls=[
        'https://book.douban.com/top250?start=0'
    ]

    rules=(
        Rule(LinkExtractor(allow=(r'https://book\.douban\.com/top250\?start=\d+')), callback='parse_item', process_request='add_cookie', follow=True),
    )

    def add_cookie(self,request):
        request.replace(cookies=[
                {'name': 'COOKIE_NAME','value': 'VALUE','domain': '.douban.com','path': '/'},
                ])
        return request

    def parse_item(self,response):
        print response
        sel=Selector(response)
        item=DoubanBookSpiderItem()

        book_name=sel.xpath('//div[@class="pl2"]/a/text()').extract()
        star=sel.xpath('//div[@class="star clearfix"]/span[@class="rating_nums"]/text()').extract()
        comment=sel.xpath('//p[@class="quote"]/span[@class="inq"]/text()').extract()

        item['book_name']=[n.encode('utf-8') for n in book_name]
        item['star']=[n.encode('utf-8') for n in star]
        item['comment']=[n.encode('utf-8') for n in comment]

        return item