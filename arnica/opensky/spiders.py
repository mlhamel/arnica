import scrapy
import json

from typing import Iterator

from arnica.opensky.items import OpenSkyItem

class OpenskySpider(scrapy.Spider):
    name = "opensky"
    allowed_domains = ["opensky-network.org"]
    start_urls = [
        'https://opensky-network.org/api/states/all'
    ]
    fields = ["icao24",  "callsign",  "origin_country",  "time_position",  "time_velocity",
              "longitude", "latitude", "altitude", "on_ground", "velocity", "heading",
              "vertical_rate", "sensors"]

    def parse(self, response) -> Iterator[OpenSkyItem]:
        jsonresponse = json.loads(response.body_as_unicode())
        for state in jsonresponse["states"]:
            item = OpenSkyItem()
            for index, field in enumerate(self.fields):
                item[field] = state[index]
                if isinstance(item[field], str):
                    item[field] = item[field].strip()
            yield item