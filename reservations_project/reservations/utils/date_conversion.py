from datetime import datetime, timedelta


class DateConversion:
    def __init__(self, date, time):
        self.date = date
        self.time = time

    @property
    def reserve_time(self):
        return datetime.combine(self.date, self.time)

    @property
    def hour_before_reserve(self):
        return (self.reserve_time - timedelta(hours=1)).time()

    @property
    def hour_after_reserve(self):
        return (self.reserve_time + timedelta(hours=1)).time()
