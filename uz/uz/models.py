from django.db import models

class Entry(models.Model):
    train = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')