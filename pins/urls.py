from django.urls import path
from . import views

urlpatterns = [
    path('', views.PinAPIView.as_view(), name='Pin API View'),
    path('upload/', views.PinImageUploadAPIView.as_view(),
         name='Pin Image Upload Api View')
]
