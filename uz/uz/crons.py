from django_cron import CronJobBase, Schedule
import logging
import random
from uz.models import Entry
import datetime
from django.utils import timezone
import requests;
from django.utils import simplejson
import time

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 15 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'uz.my_cron_job'    # a unique code

    def do(self):
        for i in range(10, 30):
            time.sleep(random.randint(5, 15))
            r=requests.post('http://booking.uz.gov.ua/purchase/search/', {'station_id_from':2200001,
                                                                          'station_id_till':2218000,
                                                                          'station_from':'Kyiv',
                                                                          'station_till':'Lviv',
                                                                          'date_start':str(i)+'.09.2012',
                                                                          'time_from':'00:00',
                                                                          'search':''})
            w=simplejson.loads(r.content);
            for train in w['value']:
                p = Entry(train=repr(train['num']), pub_date=timezone.now(),plaz=0,kupe=0,lux=0, for_date=datetime.date(2012, 9, i),s1=0,s2=0)
                for type in train['types']:
                    if(type['type_id']==1):
                        p.lux = int(type['places'])
                        #print("Lux"+str(type['places']))
                    elif(type['type_id']==3):
                        p.kupe = int(type['places'])
                    elif(type['type_id']==4):
                        p.plaz = int(type['places'])
                    elif(type['type_id']==7):
                        p.s1 = int(type['places'])
                    elif(type['type_id']==8):
                        p.s2 = int(type['places'])
                        #print("Plazkart"+str(type['places']))


            p.save()
        #logging.error("Ty huy")
