from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pin
from .serializers import PinListSerializer, PinSerializer
from .utils import save_image_to_google_cloud_storage
from authentication.decorators import authentication_required
from django.contrib.auth import get_user_model

Profile = get_user_model()


class PinAPIView(APIView):
    @authentication_required
    def post(self, request):
        try:
            jwt_user = getattr(request, 'jwt_user', None)
            serializer = PinSerializer(data=request.data)

            if serializer.is_valid():
                profile = Profile.objects.get(id=jwt_user)

                new_pin = Pin.objects.create(
                    profile=profile,
                    **serializer.validated_data
                )

                return Response(PinSerializer(new_pin).data, status=status.HTTP_201_CREATED)

        except Profile.DoesNotExist:
            return Response({'detail': 'Profile not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        pass

    def delete(self, request):
        pass

    def get(self, request):
        pins = Pin.objects.all()
        serializer = PinListSerializer(pins, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PinImageUploadAPIView(APIView):
    def post(self, request, *args, **kwargs):
        image_file = request.data.get('image')

        # Save image to Google Cloud Storage
        gs_path = save_image_to_google_cloud_storage(image_file)

        # You can store gs_path in your database or use it as needed
        # For example, you might want to save it in a model field.

        return Response({'message': 'Image uploaded successfully', 'image_url': gs_path}, status=status.HTTP_201_CREATED)
