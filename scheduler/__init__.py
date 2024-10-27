from apscheduler.schedulers.background import BackgroundScheduler

import time
from . import patrol
from . import eco_rating


def main():
    patrol.create_patrol()
    scheduler = BackgroundScheduler()
    scheduler.add_job(patrol.create_patrol, 'interval', hours=6)
    scheduler.add_job(eco_rating.create, 'interval', miniutes=1)
    scheduler.start()

    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
