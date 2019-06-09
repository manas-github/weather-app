from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'

class Person(models.Model):
    name = models.CharField(max_length=25)
    age  = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name

    
