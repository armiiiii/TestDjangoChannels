from django.views.generic import ListView, View
from django.shortcuts import render

from .models import ChatRoom


class HomeChats(ListView):
    model = ChatRoom
    template_name = 'main.html'
    context_object_name = "chats"


class ChatView(View):
    def get(self, request, *args, **kwargs):
        chatroom = ChatRoom.objects.get(uuid=kwargs.get("uuid"))
        return render(request, "chat.html", {'chatroom': chatroom})