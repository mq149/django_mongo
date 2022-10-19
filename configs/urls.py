from django.urls import path
from . import views

urlpatterns = [
    path('', views.ConfigList.as_view()),
]
