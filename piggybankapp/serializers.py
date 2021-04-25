from rest_framework import serializers
from piggybankapp.models import User, Pig


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'name', 'address', 'dob', 'phone')

class PigSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pig
        fields = ('name', 'status', 'balance', 'creationDate')

