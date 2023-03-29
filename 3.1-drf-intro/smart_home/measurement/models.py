from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Measurement(models.Model):
    temperature = models.DecimalField(max_digits=4, decimal_places=3)
    sensor = models.ForeignKey("Sensor", related_name='measurements', on_delete=models.CASCADE)
    date_of = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return f'Temperature: {self.temperature}, created at: {self.date_of}'
