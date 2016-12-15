from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.spiders import Rule,CrawlSpider
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor

from douban_mp_spider.items import DoubanMpSpiderItem

class DoubanMpSpider(CrawlSpider):
    name="douban_multiple_page_spider"
    download_delay=2
    allowed_domains=[]

    start_urls=[
        'https://movie.douban.com/top250?start=0&filter='
    ]

    rules=(
        Rule(LinkExtractor(allow=(r'https://movie\.douban\.com/top250\?start=\d+&filter=')), callback='parse_item', process_request='add_cookie', follow=True),
    )

    def add_cookie(self, request):
        request.replace(cookies=[
                {'name': 'COOKIE_NAME','value': 'VALUE','domain': '.douban.com','path': '/'},
                ])
        return request

    def parse_item(self, response):
        print response
        sel=Selector(response)
        item=DoubanMpSpiderItem()

    #cooking
        movie_name=sel.xpath('//span[@class="title"][1]/text()').extract()
        star=sel.xpath('//div[@class="star"]/span[@class="rating_num"]/text()').extract()
        comment=sel.xpath('//p[@class="quote"]/span[@class="inq"]/text()').extract()

    #Place them in dishes
        item['movie_name']=[n.encode('utf-8') for n in movie_name]
        item['star']=[n.encode('utf-8') for n in star]
        item['comment']=[n.encode('utf-8') for n in comment]

        return item


