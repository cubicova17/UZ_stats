from django_cron import CronJobBase, Schedule
import logging
from uz.models import Entry

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 5 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'uz.my_cron_job'    # a unique code

    def do(self):
        #model = Entry(train='')
        logging.error("Ty huy")
