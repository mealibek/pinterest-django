from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
import re

User = get_user_model()


class CreateProfileSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True, error_messages={'required': 'Требуется Email'}
    )

    password = serializers.CharField(
        required=True, error_messages={'required': 'Требуется Password'}
    )

    first_name = serializers.CharField(
        required=True, error_messages={'required': 'Требуется First Name'}
    )

    last_name = serializers.CharField(
        required=True, error_messages={'required': 'Требуется Last Name'}
    )

    def validate(self, data):
        """
        Validation of email existance, password pattern etc.
        """

        email = data['email']
        password = data['password']

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                'Электронная почта уже используется')

        password_pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
        if not re.match(password_pattern, password):
            raise serializers.ValidationError(
                "Неверный формат пароля. Пожалуйста, введите другой пароль.")
        return data
