from dataclasses import fields
from pyexpat import model
from sys import maxsize
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from . import models

class helloserializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""

    name=serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our userprofile oblject"""
    class Meta:
        model=models.UserProfile
        fields=('id','email','name','password')

        extra_kwargs={'password': {'write_only':True}}

    def create(self, validated_data):
        '''Create and retun a new user'''
        user =models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
############################################################################################

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """ a serializer for profile feeds items"""
    class Meta:
        model=models.ProfileFeedItem
        fields="__all__"
        extra_kwargs = {'user_profile': {'read_only': True}}

##############################Exception#######################################################        


    

       




