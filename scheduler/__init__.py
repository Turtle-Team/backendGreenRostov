from apscheduler.schedulers.background import BackgroundScheduler

import time
from . import patrol


def main():
    patrol.create_patrol()
    scheduler = BackgroundScheduler()
    scheduler.add_job(patrol.create_patrol, 'interval', minutes=30)
    scheduler.start()

    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
