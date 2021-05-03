from rest_framework import serializers
from piggybankapp.models import User, Pig, Event


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