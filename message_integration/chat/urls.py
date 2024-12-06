from django.urls import path
from . import views

app_name = "chat"
urlpatterns = [
    path('chat/', views.broadcast_sms, name='chat'),
    # path("session/lobby/", views.lobby, name="lobby"),
    # path("", views.chat, name="chat"),
    # path("session/create-message/", views.create_message, name="create-message"),
    # path("session/stream-chat-messages/", views.stream_chat_messages, name="stream-chat-messages"),
]