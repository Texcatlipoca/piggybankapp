from rest_framework import serializers
from piggybankapp.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'name', 'address', 'dob', 'phone')