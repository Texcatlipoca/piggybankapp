from django.db import models

class Customer(models.Model):
    customerId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    dob = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)


class Account(models.Model):
    accountId = models.AutoField(primary_key=True)
    accountNumber = models.CharField(max_length=200)
    balance = models.IntegerField()
    creationDate = models.DateTimeField(auto_now_add=True)
    lastUpdate = models.DateTimeField(auto_now=True)
    customer = models.OneToOneField(
      Customer,
      on_delete=models.CASCADE
    )
