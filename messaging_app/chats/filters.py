from django_filters import rest_framework as filters
from chats.models import Message
from django.contrib.auth.models import User

class MessageFilter(filters.FilterSet):
    participant = filters.ModelChoiceFilter(
        field_name='conversation__participants',
        queryset=User.objects.all(),
        label='Filter by participant username'
    )
    timestamp_gte = filters.DateTimeFilter(
        field_name='timestamp',
        lookup_expr='gte',
        label='Messages on or after this timestamp'
    )
    timestamp_lte = filters.DateTimeFilter(
        field_name='timestamp',
        lookup_expr='lte',
        label='Messages on or before this timestamp'
    )

    class Meta:
        model = Message
        fields = ['participant', 'timestamp_gte', 'timestamp_lte']