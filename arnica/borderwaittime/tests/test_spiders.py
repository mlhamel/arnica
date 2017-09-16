from pytz import timezone
from datetime import datetime
from unittest.mock import MagicMock

from django.test import TestCase

from dateutil.tz import gettz

from arnica.borderwaittime.spiders import BorderWaitTimeSpider


class TestBorderWaitTimeSpider(TestCase):
    def setUp(self):
        self.spider = BorderWaitTimeSpider()
        self.date = datetime(2017, 12, 24)
        self.localdate = timezone("America/Panama").localize(datetime(2017, 12, 24, 10, 10, 10))

    def test_parse_date(self):
        self.assertIsNone(self.spider.parse_date(''))
        self.assertEqual(self.spider.parse_date('2017-12-24'), self.date)
        self.assertEqual(self.spider.parse_date('2017-12-24 10:10:10 EST'), self.localdate)
