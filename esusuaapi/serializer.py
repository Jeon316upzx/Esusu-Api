from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from .models import EsusuGroup

class User_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','password')

    def create(self,validated_data):
        user = super(User_serializer,self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

# g_users means group users or members
class EsusuGroup_serializer(serializers.ModelSerializer):
    class Meta:
        model = EsusuGroup
        fields = ('group','group_description','g_users','amount_to_save','group_limit')
