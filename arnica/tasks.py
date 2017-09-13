import luigi
import django
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from pydoc import locate


class AbstractCrawlTask(luigi.Task):
    date = luigi.DateParameter()
    name = luigi.Parameter()

    def __init__(self, *args, **kwargs):
        super(AbstractCrawlTask, self).__init__(*args, **kwargs)

        self.spider = locate(self.name)
        self.spider_name = self.spider.__class__.__name__.lower()

    def get_filename(self):
        return self.date.strftime(f'data/{self.spider_name}-%Y_%m_%d.json')

    def output(self):
        return luigi.LocalTarget(self.get_filename())

    def run(self):
        django.setup()
        process = CrawlerProcess(get_project_settings())
        process.crawl(self.spider)
        process.start()