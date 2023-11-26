from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializers import ProfileUpdateSerializer
from rest_framework import status
from authentication.decorators import authentication_required
from django.contrib.auth import get_user_model


User = get_user_model()


class ProfileAPIView(APIView):
    @authentication_required
    def patch(self, request):
        serializer = ProfileUpdateSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            jwt_user = getattr(request, 'jwt_user', None)

            try:
                user = User.objects.get(id=jwt_user.id, email=jwt_user.email)

                update_serializer = ProfileUpdateSerializer(
                    user, data=request.data, partial=True)

                if update_serializer.is_valid():
                    update_serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(update_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            except User.DoesNotExist:
                return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @authentication_required
    def delete(self, request):
        jwt_user = getattr(request, 'jwt_user', None)

        try:
            user = User.objects.get(id=jwt_user.id, email=jwt_user.email)
            user.delete()
            user.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
