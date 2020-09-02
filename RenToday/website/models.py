from django.db import models

# Create your models here.

class Property(models.Model):
    name = models.TextField()
    desc = models.TextField()
    Type= models.TextField()
    city = models.CharField(max_length=500)
    state = models.CharField(max_length=500)
    img = models.ImageField(upload_to='pics/')
    price = models.IntegerField()


