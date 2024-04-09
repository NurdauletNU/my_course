from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=20)
    objects = models.Manager()

    def __str__(self):
        return f"{self.name}: {self.phone_num}"
