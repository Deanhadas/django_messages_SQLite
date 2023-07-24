from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Message
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
import json


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def write_message(request):
    try:
        res = json.loads(request.body)
        message = Message()
        message.sender = res["sender"]
        message.receiver = res["receiver"]
        message.message = res["message"]
        message.subject = res["subject"]
        message.save()
        return Response()
    except (json.JSONDecodeError, KeyError) as e:
        return Response({"error": "Invalid JSON or missing fields"}, status=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_messages(request):
    try:
        token = request.auth
        user = Token.objects.get(key=token).user
        all_messages = Message.objects.filter(receiver=user.username)
        messages = [message.__dict__ for message in all_messages]
        for message in messages:
            if '_state' in message.keys():
                del message['_state']
        return Response(messages)
    except Token.DoesNotExist:
        return Response({"error": "Invalid token"}, status=401)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_unread_messages(request):
    try:
        token = request.auth
        user = Token.objects.get(key=token).user
        all_messages = Message.objects.filter(receiver=user.username, is_read=False)
        messages = [message.__dict__ for message in all_messages]
        for message in messages:
            if '_state' in message.keys():
                del message['_state']
        return Response(messages)
    except Token.DoesNotExist:
        return Response({"error": "Invalid token"}, status=401)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_message(requset, message_id):
    try:
        token = requset.auth
        user = Token.objects.get(key=token).user
        message = Message.objects.get(receiver=user.username, id=message_id)
        message.is_read = True
        message.save()
        return Response(message.__json__())
    except Message.DoesNotExist:
        return Response({"error": "Message not found"}, status=404)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_message(requset, message_id):
    try:
        message = Message.objects.get(id=message_id)
        message.delete()
        return Response()
    except Message.DoesNotExist:
        return Response({"error": "Message not found"}, status=404)