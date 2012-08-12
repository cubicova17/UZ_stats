from django_cron import CronJobBase, Schedule
import logging
from uz.models import Entry
from django.utils import timezone
class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 5 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'uz.my_cron_job'    # a unique code

    def do(self):
        p = Entry(train="Ogoog", pub_date=timezone.now())
        p.save()
        logging.error("Ty huy")
