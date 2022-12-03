from datetime import datetime


class RTC:
    def __init__(self, RTC_PIN):
        self.pin = RTC_PIN

    @staticmethod
    def get_current_time_string() -> str:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return current_time

    @staticmethod
    def get_current_day() -> str:
        days = {
            1: 'MONDAY',
            2: 'TUESDAY',
            3: 'WEDNESDAY',
            4: 'THURSDAY',
            5: 'FRIDAY',
            6: 'SATURDAY',
            7: 'SUNDAY'
        }
        today = datetime.today().weekday()
        return days.get(today + 1)


if __name__ == '__main__':
    time = RTC(1).get_current_time_string()
    hour = time[:time.find(':')]
    print(hour)
    print(RTC(1).get_current_day())