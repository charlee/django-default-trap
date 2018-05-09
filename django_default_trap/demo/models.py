from django.db import models
from django.contrib.postgres.fields import JSONField


class Book(models.Model):
    name = models.CharField(max_length=255)
    detail = JSONField(editable=False, default={})