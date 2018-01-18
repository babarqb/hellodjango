from datetime import datetime

from django.db import models


class BlogModel(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField(max_length=200)
    timestamp = models.DateTimeField(datetime.now())

    def __str__(self):
        return self.title
