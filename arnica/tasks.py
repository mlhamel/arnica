import luigi
import django
import scrapy

from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

from pydoc import locate


class AbstractDjangoBasedTask(luigi.Task):
    def run(self):
        django.setup()


class AbstractCrawlTask(AbstractDjangoBasedTask):
    date = luigi.DateParameter()
    name = luigi.Parameter()

    def get_filename(self) -> str:
        spider_name = self.get_spider_name()

        return self.date.strftime(f'data/{spider_name}-%Y_%m_%d.json')

    def get_spider(self) -> scrapy.Spider:
        return locate(self.name)

    def get_spider_name(self) -> str:
        return self.spider.__class__.__name__.lower()

    def output(self) -> luigi.LocalTarget:
        return luigi.LocalTarget(self.get_filename())

    def run(self):
        super(AbstractCrawlTask, self).run()

        process = CrawlerProcess(get_project_settings())
        process.crawl(self.spider)
        process.start()