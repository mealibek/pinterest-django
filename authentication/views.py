from .utils import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from .serializers import CreateProfileSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
import binascii

User = get_user_model()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CreateProfileAPIView(APIView):
    def post(self, request, format=None):
        """
        Create profile & Return ACCESS, REFRESH Token.
        """

        serializer = CreateProfileSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            first_name = serializer.validated_data['first_name']
            last_name = serializer.validated_data['last_name']

            user = User.objects.create_user(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )

            user.save()

            hex_email = binascii.hexlify(
                email.encode('utf-8')).decode('utf-8')

            hex_password = binascii.hexlify(
                password.encode('utf-8')).decode('utf-8')

            return Response({
                'hex_email': hex_email,
                'hex_password': hex_password
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckEmailAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({
                'message': 'Email is required'
            }, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
