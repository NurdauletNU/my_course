from django.db import models


# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    objects = models.Manager()


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, db_index=True)
    patronymic = models.CharField(max_length=100)
    tabel_num = models.CharField(max_length=100, db_index=True, unique=True)
    position = models.ForeignKey(to=Position, on_delete=models.SET_NULL, null=True)
    objects = models.Manager()


class ClothCategory(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    objects = models.Manager()


class Cloth(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(to=ClothCategory, on_delete=models.SET_NULL, null=True)
    deadline = models.IntegerField()
    objects = models.Manager()


class ClothSet(models.Model):
    tabel_num = models.ForeignKey(to=Person, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    cloth_type = models.ForeignKey(to=Cloth, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    objects = models.Manager()
