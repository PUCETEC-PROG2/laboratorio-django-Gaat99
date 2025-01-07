from django.db import models

# Create your models here.
class Pokemon (models.Model):
    name = models.CharField(max_length=30, null=False) 
    type = models.CharField(max_length=30, null=False) 
    weight = models.DecimalField(decimal_places=4,max_digits=6) 
    height = models.DecimalField(decimal_places=4,max_digits=6) 

    def __str__(self):
        return self.name

class Trainer (models.Model):
    name_trainer = models.CharField(max_length=30, null=False) 
    last_name = models.CharField(max_length=30, null=False) 
    level = models.IntegerField(default=1) 
    birth = models.DateField(null=True, blank=True) 

    def __str__(self):
        return f"{self.name_trainer} - {self.last_name}"    