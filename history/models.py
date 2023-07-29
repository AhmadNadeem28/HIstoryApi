from django.db import models

class History(models.Model):
    date = models.DateField()
    food_donated = models.CharField(max_length=200)
    donated_to = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
    address = models.CharField(max_length=500,default=" ")

    def __str__(self):
      return self.food_donated
    