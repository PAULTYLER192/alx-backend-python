from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.exceptions import PermissionDenied
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from .permissions import IsParticipantOfConversation
from .pagination import MessagePagination
from .filters import MessageFilter

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsParticipantOfConversation]

    def get_queryset(self):
        # Only show conversations where the user is a participant
        return self.queryset.filter(participants=self.request.user)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsParticipantOfConversation]
    pagination_class = MessagePagination
    filterset_class = MessageFilter

    def get_queryset(self):
        # Only show messages from conversations where the user is a participant
        return Message.objects.filter(conversation__participants=self.request.user)

    def create(self, request, *args, **kwargs):
        conversation_id = request.data.get('conversation')
        if not conversation_id:
            raise PermissionDenied("conversation_id is required", code=status.HTTP_403_FORBIDDEN)
        try:
            conversation = Conversation.objects.get(id=conversation_id)
            if not conversation.participants.filter(id=request.user.id).exists():
                raise PermissionDenied("You are not a participant in this conversation", code=status.HTTP_403_FORBIDDEN)
        except Conversation.DoesNotExist:
            raise PermissionDenied("Conversation does not exist", code=status.HTTP_403_FORBIDDEN)
        return super().create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        conversation_id = request.data.get('conversation')
        if conversation_id:
            try:
                conversation = Conversation.objects.get(id=conversation_id)
                if not conversation.participants.filter(id=request.user.id).exists():
                    raise PermissionDenied("You are not a participant in this conversation", code=status.HTTP_403_FORBIDDEN)
            except Conversation.DoesNotExist:
                raise PermissionDenied("Conversation does not exist", code=status.HTTP_403_FORBIDDEN)
        return super().partial_update(request, *args, **kwargs)