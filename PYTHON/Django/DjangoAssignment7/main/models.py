from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    height = models.FloatField()  # In centimeters
    weight = models.FloatField()  # In pounds
    DIET_CHOICES = (
        ('veg', 'Vegetarian'),
        ('vegan', 'Vegan'),
        ('none', 'No preference')
    )
    diet_preference = models.CharField(max_length=5, choices=DIET_CHOICES)

    def __str__(self):
        return self.name
