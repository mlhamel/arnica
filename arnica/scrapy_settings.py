# Scrapy configuration
BOT_NAME = 'arnica'
SPIDER_MODULES = [
    'arnica.borderwaittime.spiders',
]

USER_AGENT = 'arnica (+http://arni.ca)'
ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'arnica.pipelines.ArnicaPipeline': 300,
    'arnica.borderwaittime.pipelines.BorderWaitTimePipeline': 500,
}

import django; django.setup()