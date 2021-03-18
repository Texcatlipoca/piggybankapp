from django.db import models

class User(models.Model):
    userId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    dob = models.IntegerField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"name: {self.name} , address: {self.address}"


class Profile(models.Model):
    profileId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    creationDate = models.DateTimeField(auto_now_add=True)
    lastUpdate = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=20)
    #password = models.CharField(max_length=100)


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


# add profile model
