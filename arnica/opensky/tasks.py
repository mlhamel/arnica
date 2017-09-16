from arnica.tasks import AbstractCrawlTask
from arnica.opensky.spiders import OpenskySpider


class OpenSkyCrawlTask(AbstractCrawlTask):
    spider = OpenskySpider