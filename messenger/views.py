from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view ,permission_classes
from .models import Message
#from rest_framework.permissions import IsAuthenticated
#from .serializers import MessageSerializer
#from django.core import serializers


#from rest_framework.authtoken.models import Token

import json

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def test(requset):
    mini_json={"ronron":"pop"}

    return Response(mini_json)


@api_view(['POST'])
def write_message(requset):
    res = json.loads(requset.body)
    print(res)
    message = Message()
    message.sender = res["sender"]
    print("2")
    message.receiver = res["receiver"]
    print("3")
    message.message = res["message"]
    print("4")
    message.subject = res["subject"]
    print("5")
    message.save()
    print(message)
    print(requset.body)

    return Response()


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def get_all_messages(requset,receiver):
    print(requset)
    print(receiver)
    #token = requset.auth
    #user = Token.objects.get(key=token).user
    #print(user.username)
    #all_messages = Message.objects(receiver=user.username)
    all_messages = Message.objects.filter(receiver=receiver)
    print(all_messages)
    serialized_obj = [json.dumps(message.__json__()) for message in all_messages]
    # serialized_obj = serializers.serialize('json', all_messages)
    print(serialized_obj)

    return Response(serialized_obj)

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def get_all_unread_messages(requset,receiver):
    #token = requset.auth
    #user = Token.objects.get(key=token).user
    #all_messages = Message.objects(receiver=user.username, is_read=False)
    all_messages = Message.objects.filter(receiver=receiver, is_read=False)
    print(all_messages)
    serialized_obj = [message.__json__() for message in all_messages]
    #serialized_obj = [json.dumps(message.__json__()) for message in all_messages]
    # serialized_obj = serializers.serialize('json', all_messages)
    print(serialized_obj)

    return Response(serialized_obj)




@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def read_message(requset, message_id):
    # token = requset.auth
    # user = Token.objects.get(key=token).user
    #message = Message.objects.get(receiver=user.username, id=message_id)

    message = Message.objects.get(id=message_id)
    message.is_read = True
    message.save()
    serialized_obj = json.dumps(message.__json__())
    return Response(serialized_obj)


@api_view(['DELETE'])
def delete_message(requset, message_id):

    message = Message.objects.get(id=message_id)
    message.delete()
    return Response()