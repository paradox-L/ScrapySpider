# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class DoubanMpSpiderPipeline(object):
    def open_spider(self,spider):
        self.file=codecs.open('douban_mp_movie.json', mode='wb+', encoding='utf-8')

    def process_item(self, item, spider):
        line='The top250 from doubanmovie' + '\n'
        for i in range(len(item['movie_name'])):
            movie_name={"movie_name":item['movie_name'][i]}
            star={"movie_name":item['star'][i]}
            comment={"comment":item['comment'][i]}

            line=line + json.dumps(movie_name, ensure_ascii=False)
            line=line + json.dumps(star, ensure_ascii=False)
            line=line + json.dumps(comment, ensure_ascii=False) + '\n'

        self.file.write(line)

    def close_spider(self,spider):
        self.file.close()
    	
