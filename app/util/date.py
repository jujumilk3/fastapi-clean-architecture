from datetime import datetime

from pytz import timezone


def get_now():
    return datetime.now(tz=timezone("UTC"))
