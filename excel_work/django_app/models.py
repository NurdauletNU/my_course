from django.db import models


# Create your models here.
class Products(models.Model):
    month = models.DateField()
    shop = models.CharField(max_length=100)
    count = models.IntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.CharField(max_length=100)

    objects = models.Manager()

    def __str__(self):
        return self.shop
