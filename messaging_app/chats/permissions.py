from rest_framework import permissions

class IsParticipantOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD, OPTIONS requests for all
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow write operations only if user is a participant
        return request.user in obj.participants.all()

class IsMessageSenderOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD, OPTIONS requests for all participants
        if request.method in permissions.SAFE_METHODS:
            return request.user in obj.conversation.participants.all()
        # Allow write operations only if user is the sender
        return obj.sender == request.user