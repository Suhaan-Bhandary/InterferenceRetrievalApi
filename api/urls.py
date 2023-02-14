from django.urls import path, include
from api.views import OwlClassView
from rest_framework import routers

urlpatterns = [
    path('owl/', OwlClassView.as_view())
]
