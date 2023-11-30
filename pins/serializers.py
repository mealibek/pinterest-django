from rest_framework import serializers
from .models import Pin
from profiles.models import Profile


class ProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'profile_image']


class PinListSerializer(serializers.ModelSerializer):
    profile = ProfileListSerializer()

    class Meta:
        model = Pin
        fields = '__all__'
