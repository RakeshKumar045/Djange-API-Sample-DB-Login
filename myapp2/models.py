from django.db import models


# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    salary = models.IntegerField()
    status = models.BooleanField()


class SignUp(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.CharField(max_length=130)
    phone = models.IntegerField()

    # class Meta:
    #     db_table = "signup"
