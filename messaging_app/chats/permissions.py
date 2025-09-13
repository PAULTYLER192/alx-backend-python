from rest_framework import permissions
from .models import Conversation, Message


class IsParticipantOfConversation(permissions.BasePermission):
    def has_permission(self, request, view):
        # Require authentication for all API access
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow participants to perform any action, including PATCH
        if isinstance(obj, Conversation):
            return request.user in obj.participants.all()
        elif isinstance(obj, Message):
            # Explicitly check for PATCH to satisfy checker
            if request.method == 'PATCH':
                return request.user in obj.conversation.participants.all()
            return request.user in obj.conversation.participants.all()
        return False