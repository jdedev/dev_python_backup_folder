import time
from datetime import datetime
from crontab import CronTab

cron_string = "* * * * *"  # Every 2 minutes
cron = CronTab(cron_string)


def my_function():
    print("Function executed at:", datetime.now())


while True:
    now = datetime.now()
    if cron.test(now):  # Check if current time matches cron schedule
        my_function()
        time.sleep(1)  # Prevent multiple triggers within the same minute
    else:
        print(datetime.now())

    time.sleep(1)  # Avoid busy waiting
