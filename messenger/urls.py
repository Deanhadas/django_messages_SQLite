from django.urls import path
from .views import *

urlpatterns = [
    path('write/', write_message, name='write_message'),
    path('messages-received/', get_all_messages_as_receiver, name='get_all_messages_as_receiver'),
    path('messages-sent/', get_all_messages_as_sender, name='get_all_messages_as_sender'),
    path('unread-messages/', get_all_unread_messages, name='get_unread_messages'),
    path('read-message/<str:message_id>/', read_message, name='read_message'),
    path('del-message/<str:message_id>/', delete_message, name='delete_message'),
]
