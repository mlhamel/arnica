from pytz import common_timezones, timezone

from datetime import datetime
from dateutil.tz import gettz

from typing import Iterator, Optional, Tuple

def gen_tzinfos() -> Iterator[Tuple[Optional[str], object]]:
    for zone in common_timezones:
        try:
            tzdate = timezone(zone).localize(datetime.utcnow(), is_dst=None)
        except Exception:
            pass
        else:
            tzinfo = gettz(zone)

            if tzinfo:
                yield tzdate.tzname(), tzinfo