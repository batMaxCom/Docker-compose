from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Sensor(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=200, blank=True)


class Measurement(models.Model):
    sensor = models.ForeignKey(
        Sensor,
        on_delete=models.CASCADE,
        related_name='measurements'
    )
    temperature = models.FloatField(
        validators=[MinValueValidator(-100),
                    MaxValueValidator(100)]
    )
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='measurement/images/', blank=True)
