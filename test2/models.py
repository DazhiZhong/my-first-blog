from django.db import models

# Create your models here.


class dosomething(models.Model):
    title = models.TextField(blank=True)
    shit = models.TextField(blank=True)
    ass = models.TextField(blank=True)
    bigshit = models.TextField(blank=True)
    time = models.DateTimeField(blank=True,null=True)
