from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name',
                  'last_name', 'profile_image')
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
            'profile_image': {'required': False},
        }
