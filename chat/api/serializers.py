from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('id', 'text', 'sender', 'recipient')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')
