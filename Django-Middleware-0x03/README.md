ALX Backend Python: Messaging App
A Django REST Framework (DRF) backend for a messaging application with JWT authentication.
Table of Contents

Project Overview
Features
Tech Stack
Setup Instructions
Database Seeding
API Documentation
API Endpoints
Using auth-helper.ps1
Troubleshooting
Contributing
License

Project Overview
This project is a backend API for a messaging application, allowing users to authenticate and manage messages/conversations. It uses Django REST Framework with JWT authentication.
Features

JWT Authentication: Secure user authentication using JSON Web Tokens with custom claims (username, email).
Conversations: Create and manage conversations between users.
Messages: Send, view, update, and delete messages within conversations, with access restricted to participants.
Permissions: Custom IsParticipantOfConversation ensures only authenticated participants can perform actions (GET, POST, PUT, PATCH, DELETE), with explicit checks for POST, PUT, PATCH, and DELETE methods.
Pagination: Messages API returns 20 messages per page, with customizable page size.
Filtering: Filter messages by participant (user in conversation) or timestamp range using django-filter.
Seeding: Populate database with sample users, conversations, and messages.
API Documentation: Swagger and Redoc interfaces for easy API exploration.
auth-helper.ps1: PowerShell script to manage JWT tokens and API calls.

Tech Stack

Backend: Django 5.2.6, Django REST Framework
Authentication: djangorestframework-simplejwt
Documentation: drf-yasg
Filtering: django-filter
Database: SQLite (initial setup)
Environment: django-environ
Python: 3.13.7
OS: Windows (tested), Linux/Mac compatible

Setup Instructions

Clone the Repository:
git clone https://github.com/PAULTYLER192/alx-backend-python.git
cd alx-backend-python/messaging_app


Set Up Virtual Environment:
python -m venv venv
.\venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt


Set Up Environment Variables:

Copy .env.example to .env:copy .env.example .env


Edit .env with:SECRET_KEY=your_secure_key_here
DJANGO_API_BASE_URL=http://127.0.0.1:8000
DJANGO_API_USERNAME=airbnb_user
DJANGO_API_PASSWORD=favor@254




Apply Migrations:
python manage.py migrate


Create Superuser:
python manage.py createsuperuser


Run Server:
python manage.py runserver


Admin panel: http://127.0.0.1:8000/admin/.
API: http://127.0.0.1:8000/api/.
Swagger: http://127.0.0.1:8000/swagger/.
Redoc: http://127.0.0.1:8000/redoc/.



Database Seeding
Populate the database with sample users, conversations, and messages:
python manage.py seed


Creates 3 users (airbnb_user, testuser, user3).
Creates 3+ conversations with 2-3 random participants.
Adds 2-5 messages per conversation.
Verify in admin panel or via:python manage.py shell

from chats.models import Conversation, Message
print(Conversation.objects.count())
print(Message.objects.count())



API Documentation
Explore the API using Swagger or Redoc:

Swagger UI: http://127.0.0.1:8000/swagger/ (interactive interface to test endpoints).
Redoc: http://127.0.0.1:8000/redoc/ (static documentation).
Authenticate in Swagger by clicking "Authorize" and entering Bearer <access_token>.

API Endpoints
All endpoints require JWT authentication and participant status for access. Use the access token from auth-helper.ps1.

POST /api/token/: Obtain JWT access and refresh tokens with custom claims.. .\auth-helper.ps1
$tokens = Get-ValidTokens
Write-Output "Access Token: $($tokens.access)"


POST /api/token/refresh/: Refresh access token.. .\auth-helper.ps1
$tokens = Refresh-Tokens $tokens.refresh


GET/POST /api/chats/conversations/: List or create conversations (participants only).. .\auth-helper.ps1
Invoke-Api -endpoint "/api/chats/conversations/" -method Post -body @{participant_ids=@(2)}


GET/PUT/DELETE /api/chats/conversations//: Retrieve, update, or delete a conversation (participants only).
GET/POST /api/chats/messages/: List or create messages (participants only).
Supports pagination (?page=2, ?page_size=10) and filtering (?participant=2, ?timestamp_gte=2025-09-12T00:00:00Z).

. .\auth-helper.ps1
Invoke-Api -endpoint "/api/chats/messages/" -method Post -body @{conversation=1; content="Hello, how are you?"}
Invoke-Api -endpoint "/api/chats/messages/?participant=2&timestamp_gte=2025-09-12T00:00:00Z" -method Get


GET/PUT/PATCH/DELETE /api/chats/messages//: Retrieve, update, partially update, or delete a message (participants only).. .\auth-helper.ps1
Invoke-Api -endpoint "/api/chats/messages/1/" -method Put -body @{conversation=1; content="Updated via PUT"}
Invoke-Api -endpoint "/api/chats/messages/1/" -method Patch -body @{content="Updated via PATCH"}
Invoke-Api -endpoint "/api/chats/messages/1/" -method Delete



Using auth-helper.ps1
The auth-helper.ps1 script simplifies JWT token management:

Set environment variables in .env:DJANGO_API_BASE_URL=http://127.0.0.1:8000
DJANGO_API_USERNAME=airbnb_user
DJANGO_API_PASSWORD=favor@254


Source the script:. .\auth-helper.ps1


Use Invoke-Api for authenticated requests, as shown in API Endpoints.

Troubleshooting

Permission Denied (403):
Ensure user is authenticated and a participant:. .\auth-helper.ps1
Invoke-Api -endpoint "/api/chats/messages/1/" -method Get


Check REST_FRAMEWORK in settings.py includes IsParticipantOfConversation.


Token Not Valid:
Verify .env has correct DJANGO_API_USERNAME and DJANGO_API_PASSWORD.
Refresh tokens:. .\auth-helper.ps1
Get-ValidTokens




Serializer Error ("conversation" required):
Use conversation (not conversation_id):Invoke-Api -endpoint "/api/chats/messages/" -method Post -body @{conversation=1; content="Test"}




Empty Sender Field:
Verify MessageSerializer in chats/serializers.py sets sender:python manage.py shell

from chats.models import Message
print(Message.objects.all().values('id', 'sender__username'))




Pagination Issues:
Verify chats/pagination.py sets page_size = 20 and MessageViewSet uses MessagePagination.
Test: Invoke-Api -endpoint "/api/chats/messages/?page=2" -method Get.


Filtering Issues:
Verify chats/filters.py defines MessageFilter with participant, timestamp_gte, and timestamp_lte.
Test: Invoke-Api -endpoint "/api/chats/messages/?participant=2" -method Get.


User Not Found:
Verify users:python manage.py shell

from django.contrib.auth.models import User
print(User.objects.all())




SyntaxError in init.py:
Ensure chats/management/__init__.py and chats/management/commands/__init__.py are empty:Set-Content -Path chats\management\__init__.py -Value "" -Encoding UTF8
Set-Content -Path chats\management\commands\__init__.py -Value "" -Encoding UTF8





Contributing

Fork the repository.
Create a feature branch (git checkout -b feature/your-feature).
Commit changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a pull request.

License
MIT License