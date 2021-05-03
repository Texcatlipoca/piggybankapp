from rest_framework import serializers
from piggybankapp.models import User, Pig, Reminder


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('name', 'address', 'dob', 'phone')

class PigSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pig
        fields = ('name', 'status', 'balance', 'creationDate')

class ReminderSerializer(serializers.ModelSerializer):

    class Meta:
        mdoel = Reminder
        fields = ('name', 'date', 'reminderType', 'medium', 'status')

        