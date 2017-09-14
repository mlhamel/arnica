# -*- coding: utf-8 -*-
import logging

from django.db.utils import IntegrityError

from datadog import statsd

logger = logging.getLogger(__name__)


class ArnicaPipeline(object):
    def _exception_raised(self, item, e):
        logger.error(f"Duplicate {item.__class__.__name__}: %s", item)
        statsd.increment('arnicas-integrity-error', tags=dict(**item))

    def process_item(self, item, spider):
        try:
            item.save()
        except IntegrityError as e:
            self._exception_raised(item, e)
        return item