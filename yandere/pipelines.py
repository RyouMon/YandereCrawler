# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from urllib.parse import unquote
from scrapy.pipelines.images import ImagesPipeline


class YandereImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        return scrapy.Request(item['file_url'])

    def file_path(self, request, response=None, info=None, *, item=None):
        # Using original filename
        return unquote(request.url.rsplit('/', 1)[-1])
