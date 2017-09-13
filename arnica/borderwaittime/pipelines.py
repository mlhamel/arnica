import logging

from django.db.utils import IntegrityError

from datadog import statsd

from arnica.borderwaittime.items import BorderWaitTimeItem
from arnica.borderwaittime.models import Tick

logger = logging.getLogger(__name__)

class BorderWaitTimePipeline(object):
    def _exception_raised(self, item, e):
        logger.error('Duplicate BorderWaitTime::Tick: %s', item)
        statsd.increment('border-wait-time-tick-integrity-error', tags=dict(**item))

    def process_item(self, item, spider):
        try:
            tick = item.save()
        except IntegrityError as e:
            self._exception_raised(item, e)
        return item
