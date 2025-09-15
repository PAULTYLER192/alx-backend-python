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
            # For safe methods (GET, HEAD, OPTIONS), allow participants
            if request.method in permissions.SAFE_METHODS:
                return request.user in obj.conversation.participants.all()

            # For modifications (POST, PUT, PATCH, DELETE), allow only participants
            if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
                return request.user in obj.conversation.participants.all()

        return False