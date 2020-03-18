from django.db import models

class latlng(models.Model):
    Latitude = models.CharField(max_length=20)
    Longitude = models.CharField(max_length=20)

    