from django.urls import path

from .views import HomeChats, ChatView

app_name = 'chat'
urlpatterns = [
   path("", HomeChats.as_view(), name="home"),
   path("<uuid:uuid>/", ChatView.as_view(), name="group")
]