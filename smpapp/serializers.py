from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class Userserializer(serializers.Serializer):

    class meta:
        model = User
        fields=['username','password']






class FacebookSerializers(serializers.ModelSerializer):
    class Meta:
        model=Facebook
        fields=['username','age','id']


        def valid(self,data):


            if data ['age'] < 18 :
             raise serializers.ValidationError({'error':'age should be greater 18'})

            # if data['username']:
            #    for i in data['username']:
            #       if i.isdigit():
            #  raise serializers.ValidationError({'error':'user name cannot be numeric'})





class Profileserializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['name', 'profile_img', 'cover_img']

