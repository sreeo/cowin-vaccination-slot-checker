import schedule
import time
from vaccination_slots import find_slots

def job():
    find_slots()

schedule.every(1).minutes.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
