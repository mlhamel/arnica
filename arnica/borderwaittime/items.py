import scrapy

from scrapy_djangoitem import DjangoItem

from arnica.borderwaittime.models import Tick

class BorderWaitTimeItem(DjangoItem):
    django_model = Tick