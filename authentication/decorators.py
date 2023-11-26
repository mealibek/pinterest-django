from functools import wraps
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.authentication import JWTAuthentication

User = get_user_model()
JWT_authenticator = JWTAuthentication()


def authentication_required(view_func):
    @wraps(view_func)
    def wrapper(self, *args, **kwargs):
        response = JWT_authenticator.authenticate(self.request)
        if response is not None:
            user = response[0]
            self.request.jwt_user = user
            return view_func(self, *args, **kwargs)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    return wrapper
