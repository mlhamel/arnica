import scrapy

from typing import Iterator
from datetime import datetime
from dateutil import parser

from arnica.borderwaittime.items import BorderWaitTimeItem
from arnica.lib.timezone import gen_tzinfos


class BorderWaitTime(scrapy.Spider):
    name = 'border-wait-time'
    allowed_domains = ['www.cbsa-asfc.gc.ca']
    start_urls = [
        'http://www.cbsa-asfc.gc.ca/bwt-taf/menu-eng.html'
    ]

    def parse_date(self, value) -> datetime:
        if not value:
            return None
        return parser.parse(value, tzinfos=dict(gen_tzinfos()))

    def parse(self, response) -> Iterator[BorderWaitTimeItem]:
        for tr in response.css('table#bwttaf tbody tr'):
            item = BorderWaitTimeItem()
            item['office'] = tr.css('th::text').extract_first()
            item['commercial_flow'] = tr.css('td:nth-of-type(1)::text').extract_first()
            item['travellers_flow'] = tr.css('td:nth-of-type(2)::text').extract_first()
            item['updated'] = self.parse_date(tr.css('td time::text').extract_first())

            yield item
