from django.db import models


class Task1(models.Model):
    words1 = models.TextField()
    words2 = models.CharField(max_length=15)


class Task2(models.Model):
    massiv = models.CharField(max_length=100)
    target = models.CharField(max_length=2)
