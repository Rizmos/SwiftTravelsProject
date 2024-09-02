from django.db import models

# Create your models here.
class Member(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.fullname

class Premium(models.Model):
    name = models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    amount=models.IntegerField()



    def __str__(self):
        return self.name

class Basic(models.Model):
    name = models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    amount=models.IntegerField()

    def __str__(self):
        return self.name

class Plus(models.Model):
    fullname = models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    amount=models.IntegerField()

    def __str__(self):
        return self.name

class Shipment(models.Model):
    fullname = models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    origin=models.CharField(max_length=200)
    destination=models.CharField(max_length=200)
    date=models.DateField()
    message=models.CharField(max_length=100000)

    def __str__(self):
        return self.fullname




