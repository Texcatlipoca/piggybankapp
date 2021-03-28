from django.db import models

class User(models.Model):
    userId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    dob = models.IntegerField()
    phone = models.CharField(max_length=20)
    test = models.CharField(max_length=100) #not sure

    def __str__(self):
        return f"name: {self.name} , address: {self.address}"


class Pig(models.Model):
    pigId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    balance = models.IntegerField()
    creationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"name: {self.name} , balance: {self.balance}, status: {self.status}"


class Event(models.Model):
    eventId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    summary = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return f"name: {self.name} , date: {self.date}"

class Reminder(models.Model):
    reminderId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    date = models.DateTimeField()
    type = models.CharField(max_length=50)
    medium = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"name: {self.name} , date: {self.date}, medium: {self.medium}"


class Goal(models.Model):
    userId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    startingBalance = models.IntegerField(default=0)
    endingBalance = models.IntegerField()
    currentBalance = models.IntegerField(default=0)


    def __str__(self):
        return f"name: {self.name} , status: {self.status}, balance :{self.currentBalance}"


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
    user = models.OneToOneField(
      User,
      on_delete=models.CASCADE
    )

class Peer(User):
    relation = models.CharField(max_length=100) #not sure
