from django.db import models
from django.urls import reverse

# Create your models here.


class breakfastho(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.TextField()
    Price = models.DecimalField(max_digits=6,decimal_places=2,blank=True, null=True)
    def get_absolute_url(self):
        return reverse("bf:b_number", kwargs={"b_id": self.id}) # b_id used in urls
    
    