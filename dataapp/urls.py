from django.urls import path
from dataapp import views

urlpatterns = [
    path('', views.ViewProfile.as_view(), name = 'homepage')
]
