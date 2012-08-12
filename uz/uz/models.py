from django.db import models

class Entry(models.Model):
    train = models.CharField(max_length=50)
    plaz = models.IntegerField()
    kupe = models.IntegerField()
    lux = models.IntegerField()
    s1 = models.IntegerField()
    s2 = models.IntegerField()
    for_date = models.DateField()
    pub_date = models.DateTimeField('date published')