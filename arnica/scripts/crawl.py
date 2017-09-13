import click
import django

from luigi.retcodes import run_with_retcodes

from datetime import datetime

from arnica.lib.environment import modified_environ

@click.command()
@click.option('--date', help='Timestamp of the day.')
@click.option('--name', help='Name of the task to run.')
def main(date, name):
    """Task runner for luigi crawl task system for arnica"""
    if date is None:
        date = datetime.today().strftime('%Y-%m-%d')
    with modified_environ(DJANGO_SETTINGS_MODULE='arnica.settings'):
        django.setup()
        run_with_retcodes([
            '--module', 'arnica.tasks', 'AbstractCrawlTask',
            '--date', date,
            '--name', name,
        ])

if __name__ == '__main__':
    main()