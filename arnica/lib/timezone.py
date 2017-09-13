import pytz
from datetime import datetime
from dateutil.tz import gettz


def gen_tzinfos():
    for zone in pytz.common_timezones:
        try:
            tzdate = pytz.timezone(zone).localize(datetime.utcnow(), is_dst=None)
        except pytz.NonExistentTimeError:
            pass
        else:
            tzinfo = gettz(zone)

            if tzinfo:
                yield tzdate.tzname(), tzinfo