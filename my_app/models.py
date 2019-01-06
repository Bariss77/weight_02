#-*- coding: utf-8 -*-
from django.db import models
from datetime import datetime


class Weight(models.Model):
    weight = models.CharField(max_length=5)
    date = models.DateTimeField(default=datetime.now())

    def _str__(self):
        return self.weight

class Food(models.Model):
    title = models.CharField(max_length=100)
    weight_food = models.CharField(max_length=5)

    def __str__(self):
        return self.title
