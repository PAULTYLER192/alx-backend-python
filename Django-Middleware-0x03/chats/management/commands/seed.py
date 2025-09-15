from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from chats.models import Conversation, Message
import random

class Command(BaseCommand):  # 👈 Django looks for this
    help = "Seed the database with sample conversations and messages"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Starting database seeding..."))

        # Users
        users = [
            {"username": "airbnb_user", "email": "ochiengpaul193@gmail.com", "password": "favor@254"},
            {"username": "testuser", "email": "test@example.com", "password": "testpass"},
            {"username": "user3", "email": "user3@example.com", "password": "user3pass"},
        ]

        created_users = []
        for user_data in users:
            user, created = User.objects.get_or_create(
                username=user_data["username"],
                defaults={"email": user_data["email"]}
            )
            if created:
                user.set_password(user_data["password"])
                user.save()
                self.stdout.write(self.style.SUCCESS(f"Created user: {user.username}"))
            created_users.append(user)

        # Conversations
        conversations = []
        for i in range(3):
            conv = Conversation.objects.create()
            participants = random.sample(created_users, k=random.randint(2, 3))
            conv.participants.set(participants)
            conv.save()
            conversations.append(conv)
            self.stdout.write(self.style.SUCCESS(
                f"Created conversation {conv.id} with {len(participants)} participants"
            ))

        # Messages
        for conv in conversations:
            for i in range(random.randint(2, 5)):
                sender = random.choice(list(conv.participants.all()))
                Message.objects.create(
                    conversation=conv,
                    sender=sender,
                    content=f"Sample message {i+1} from {sender.username} in conversation {conv.id}"
                )
            self.stdout.write(self.style.SUCCESS(f"Added messages to conversation {conv.id}"))

        self.stdout.write(self.style.SUCCESS("Database seeding completed!"))
