from django.urls import include, path
from .views import RoomView


urlpatterns = [
    path("room/", RoomView.as_view()),
]
