
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from arnica.borderwaittime.items import BorderWaitTimeItem
from arnica.borderwaittime.pipelines import BorderWaitTimePipeline


class ArnicaPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, BorderWaitTimeItem):
            pipeline = BorderWaitTimePipeline()
            pipeline.process_item(item, spider)
        return item