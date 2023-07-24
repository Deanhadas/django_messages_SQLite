from django.urls import path
from .views import *

urlpatterns = [
    path('write/', write_message, name='write_message'),
    path('messages/<str:receiver>/', get_all_messages, name='get_all_messages'),
    path('unread-messages/<str:receiver>/', get_all_unread_messages, name='get_unread_messages'),
    path('read-message/<str:message_id>/', read_message, name='read_message'),
    path('del-message/<str:message_id>/', delete_message, name='delete_message'),

    path('test/', test, name='delete_message'),

]
