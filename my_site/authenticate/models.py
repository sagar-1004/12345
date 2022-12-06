from django.db import models

# Create your models here.


class stud(models.Model):
    _id = models.AutoField(primary_key=True)
    prn = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.prn


class student(models.Model):
    _id = models.AutoField(primary_key=True)
    prn = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
