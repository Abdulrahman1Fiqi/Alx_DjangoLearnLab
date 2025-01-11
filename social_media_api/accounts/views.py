from rest_framework import serializers
from .models import CustomUser   
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration and profile management.
    """
    class Meta:
        model = CustomUser   
        fields = ('id', 'username', 'email', 'bio', 'profile_picture', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Create a new user with a hashed password and return the user.
        """
        user = get_user_model().objects.create_user(**validated_data)  # Use get_user_model to create user
        return user

class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    """
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        """
        Validate the user credentials.
        """
        user = authenticate(**attrs)
        if user is None:
            raise serializers.ValidationError('Invalid credentials')
        # Create a token for the user if it doesn't exist
        token, created = Token.objects.get_or_create(user=user)
        return token.key  # Return the token key