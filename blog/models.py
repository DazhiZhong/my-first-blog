from django.db import models
from django.urls import reverse
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    body = models.TextField()
    image = models.ImageField(upload_to='assets/', blank=False,null=True)
    payment = models.ImageField(upload_to='assets/', height_field=None, width_field=None, max_length=None)
    def get_absolute_url(self):
        return reverse("Blog:blog_detail", kwargs={"blog_id": self.id})
    def get_id(self):
        return self.id
        
class Users(models.Model):
    username = models.CharField(max_length=50)
    #password = models.CharField(max_length=50)
    


