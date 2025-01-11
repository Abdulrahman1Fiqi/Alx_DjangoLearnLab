from rest_framework import serializers
from .models import CustomUser 
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser 
        fields = ('id', 'username', 'email', 'bio', 'profile_picture')

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user is None:
            raise serializers.ValidationError('Invalid credentials')
        return user