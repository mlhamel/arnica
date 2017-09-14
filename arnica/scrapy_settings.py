# Scrapy configuration
BOT_NAME = 'arnica'
SPIDER_MODULES = [
    'arnica.borderwaittime.spiders',
    'arnica.opensky.spiders',
]

USER_AGENT = 'arnica (+http://arni.ca)'
ROBOTSTXT_OBEY = True
AUTOTHROTTLE_ENABLED = True

ITEM_PIPELINES = {
    'arnica.pipelines.ArnicaPipeline': 300,
}

import django; django.setup()