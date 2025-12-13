class Time:
    def __init__(self, hour=12, minute=0, second=0, am_pm="AM"):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.am_pm = am_pm

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d} {self.am_pm}"