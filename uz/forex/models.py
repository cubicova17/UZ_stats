from django.db import models


class DocumentCSV(models.Model):
    docfile = models.FileField(upload_to='data/')
