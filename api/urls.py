from django.urls import path, include
from api.views import OwlClassView, UserQueryClass
from rest_framework import routers

urlpatterns = [
    path('owl/', OwlClassView.as_view()),
    path('query/', UserQueryClass.as_view()),
]
