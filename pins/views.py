from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pin
from .serializers import PinListSerializer


class PinAPIView(APIView):
    def post(self, request):
        pass

    def patch(self, request):
        pass

    def delete(self, request):
        pass

    def get(self, request):
        pins = Pin.objects.all()
        serializer = PinListSerializer(pins, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
