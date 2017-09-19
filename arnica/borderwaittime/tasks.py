from arnica.tasks import AbstractCrawlTask, AbstractDjangoBasedTask
from arnica.borderwaittime.spiders import BorderWaitTimeSpider


class BorderWaitTimeCrawlTask(AbstractCrawlTask):
    spider = BorderWaitTimeSpider


class BorderWaitStatPerHour(AbstractDjangoBasedTask):
    def requires(self):
        return [BorderWaitTimeCrawlTask]

    def run(self):
        pass
