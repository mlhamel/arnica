import scrapy

from scrapy_djangoitem import DjangoItem

from arnica.opensky.models import State

class OpenSkyItem(DjangoItem):
    django_model = State