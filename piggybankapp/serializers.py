from rest_framework import serializers
from piggybankapp.models import Goal, User, Pig, Event, Reminder, Goal, Profile



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('name', 'address', 'dob', 'phone')

class PigSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pig
        fields = ('name', 'status', 'balance', 'creationDate')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'summary', 'date')

class ReminderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reminder
        fields = ('name', 'date', 'reminderType', 'medium', 'status')

class GoalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goal
        fields = ('name', 'status', 'startingBalance', 'endingBalance', 'currentBalance')

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('username', 'creationDate', 'lastUpdate', 'phone')

