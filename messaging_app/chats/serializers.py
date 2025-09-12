from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    conversation_id = serializers.PrimaryKeyRelatedField(
        queryset=Conversation.objects.all(), source='conversation', write_only=True
    )

    class Meta:
        model = Message
        fields = ['id', 'conversation', 'conversation_id', 'sender', 'content', 'timestamp']
        read_only_fields = ['sender', 'timestamp']

    def create(self, validated_data):
        validated_data['sender'] = self.context['request'].user
        return super().create(validated_data)

class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    participant_ids = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True, write_only=True
    )
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['id', 'participants', 'participant_ids', 'messages', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        participant_ids = validated_data.pop('participant_ids')
        conversation = Conversation.objects.create()
        conversation.participants.set(participant_ids)
        conversation.participants.add(self.context['request'].user)
        return conversation