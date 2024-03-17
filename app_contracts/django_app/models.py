from django.db import models
from django.contrib.auth.models import User


class Agent(models.Model):
    bin = models.CharField(max_length=24, unique=True, null=False, blank=True, db_index=True)
    title = models.CharField(max_length=255, db_index=True)
    objects = models.Manager()


class Comment(models.Model):
    comment = models.CharField(max_length=255, db_index=False)
    is_good = models.BooleanField(default=True)
    objects = models.Manager()


class Contract(models.Model):
    agent_id = models.ForeignKey(to=Agent, related_name='contracts', on_delete=models.SET_NULL, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(db_index=True)
    comment_id = models.ForeignKey(to=Comment, blank=True, on_delete=models.SET_NULL, null=True)
    file_path = models.FileField(upload_to='files/', null=True, blank=True)
    author = models.ForeignKey(to=User, related_name='contracts', on_delete=models.SET_NULL, null=True)
    objects = models.Manager()
