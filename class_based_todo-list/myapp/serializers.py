from rest_framework import serializers
from .models import TodoItem
from django.contrib.auth.models import User

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def register(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email= validated_data['email'],
            #at this point we can add every additional fields we want for the registration
        )
        return user
    
    class Meta:
        model = User
        fields = ['username' , 'password' , 'email']
        