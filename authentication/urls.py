from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)
from .views import MyTokenObtainPairView, CreateProfileAPIView, CheckEmailAPIView, AuthInfoAPIView

urlpatterns = [
    path('', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('create/', CreateProfileAPIView.as_view(), name='create_profile'),
    path('email-check/', CheckEmailAPIView.as_view(), name='check_email'),
    path('info/', AuthInfoAPIView.as_view(), name='auth_info')
]
