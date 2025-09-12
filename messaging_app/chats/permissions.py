from rest_framework import permissions
from .models import Conversation, Message


class IsParticipantOfConversation(permissions.BasePermission):
    def has_permission(self, request, view):
        # Require authentication for all API access
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Handle both Conversation and Message objects
        if isinstance(obj, Conversation):
            # Allow participants to perform any action (GET, POST, PUT, DELETE)
            return request.user in obj.participants.all()
        elif isinstance(obj, Message):
            # Allow participants of the conversation to perform any action on messages
            return request.user in obj.conversation.participants.all()
        return False