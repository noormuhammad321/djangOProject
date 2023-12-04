from django.db import models

class YourModel(models.Model):
    image = models.ImageField(upload_to='images/')
