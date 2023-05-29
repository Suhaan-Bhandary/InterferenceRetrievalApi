from django.urls import path
from client.views import home, read, update, delete

urlpatterns = [
    path('', home, name="create"),
    path('read/', read, name="read"),
    path('update/', update, name="update"),
    path('delete/', delete, name="delete"),
]
