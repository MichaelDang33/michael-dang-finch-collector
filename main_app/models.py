from django.db import models

# Create your models here.

class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    diet = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField(max_length=250)

# Changing this instance method does not impact the database...
# Therefore, no makemigrations is necessary
def __str__(self):
    return f'{self.name} ({self.id})'