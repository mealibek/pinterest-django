from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# import secrets
# import string


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        user = self.user

        data['id'] = user.id
        data['email'] = user.email
        data['first_name'] = user.first_name
        data['last_name'] = user.last_name
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        return data
