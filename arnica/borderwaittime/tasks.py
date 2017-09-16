from arnica.tasks import AbstractCrawlTask, AbstractDjangoBasedTask
from arnica.borderwaittime.spiders import BorderWaitTimeSpider


class BorderWaitTimeCrawlTask(AbstractCrawlTask):
    spider = BorderWaitTimeSpider


class BorderWaitStatPerHour(AbstractDjangoBasedTask):
    pass
