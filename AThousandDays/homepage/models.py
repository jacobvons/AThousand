from django.db import models
from rest_framework import viewsets


# Create your models here.
class Word(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    by = models.CharField(max_length=30)
    img = models.ImageField(blank=True, null=True)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Photo(models.Model):
    title = models.CharField(max_length=50)
    by = models.CharField(max_length=30)
    date = models.DateField(blank=True, null=True)
    img = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Food(models.Model):
    title = models.TextField()
    date = models.DateField(blank=True, null=True)
    description = models.TextField()
    by = models.TextField()
    img = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    img = models.ImageField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Place(models.Model):
    title = models.CharField(max_length=50)
    address = models.TextField()
    img = models.ImageField(blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Music(models.Model):
    title = models.CharField(max_length=50)
    by = models.CharField(max_length=50)
    date = models.DateField(blank=True, null=True)
    description = models.TextField()
    img = models.ImageField(blank=True, null=True)
    src = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
