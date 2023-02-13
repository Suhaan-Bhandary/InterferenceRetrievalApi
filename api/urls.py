from django.urls import path, include
from api.views import OwlClass
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'owl-class', OwlClass)

urlpatterns = [
  path('', include(router.urls))
]
