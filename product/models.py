from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=211)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.title