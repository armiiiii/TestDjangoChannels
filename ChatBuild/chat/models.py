from uuid import uuid4

from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()


class ChatRoom(models.Model):
    uuid = models.UUIDField(default=uuid4)
    name = models.CharField(max_length=30)
    users = models.ManyToManyField(User)

    def __str__(self) -> str:
        return f"Group {self.name}-{self.uuid}"

    def get_absolute_url(self):
        return reverse("group", args=[str(self.uuid)])

    def add_user_to_group(self, user):
        self.users.add(user)
        self.event_set.create(type='Join', user=user)
        self.save()

    def delete_user_from_group(self, user):
        self.users.delete(user)
        self.event_set.create(type='Left', user=user)
        self.save()


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author}: {self.text}"


class Event(models.Model):
    CHOICES = [
        ("Join", "join"),
        ("Left", "left")
    ]
    
    type = models.CharField(choices=CHOICES, max_length=10)
    description= models.CharField(max_length=50, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    chatroom = models.ForeignKey(ChatRoom ,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.description = f"{self.user} {self.type} the {self.chatroom.name} group"
        super().save(*args, kwargs)

    def __str__(self) -> str:
        return f"{self.description}"
    