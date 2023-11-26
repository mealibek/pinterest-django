from django.urls import path
from . import views

urlpatterns = [
    path('', views.PinAPIView.as_view(), name='Pin API View')
]
