from django.db import models

# Create your models here.

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)  
    weight = models.FloatField(null=True, blank=True)  
    level = models.IntegerField(default=1)  
    birth = models.DateField(null=True, blank=True)  
    picture = models.ImageField(upload_to='trainers/')  

    def __str__(self):
        return f"{self.name} {self.last_name if self.last_name else ''}"   

class Pokemon (models.Model):
    name = models.CharField(max_length=30, null=False) 
    type = models.CharField(max_length=30, null=False) 
    weight = models.DecimalField(decimal_places=4,max_digits=6) 
    height = models.DecimalField(decimal_places=4,max_digits=6) 
    trainer = models.ForeignKey(Trainer, on_delete = models.SET_NULL,null=True)
    picture = models.ImageField(upload_to="pokemon_images")   

    def __str__(self):
        return self.name
