# ALX Backend Python: Messaging App  

A Django REST Framework (DRF) backend for a messaging application with JWT authentication.  

---

## Table of Contents
- Project Overview  
- Features  
- Tech Stack  
- Setup Instructions  
- Database Seeding  
- API Endpoints  
- Troubleshooting  
- Contributing  
- License  

---

## Project Overview  
This project is a backend API for a messaging application, allowing users to authenticate and manage messages/conversations. It uses Django REST Framework with JWT authentication.  

---

## Features
- **JWT Authentication**: Secure user authentication using JSON Web Tokens.  
- **Conversations**: Create and manage conversations between users.  
- **Messages**: Send and view messages within conversations, with access restricted to participants.  
- **Permissions**: Users can only access their own conversations and messages.  
- **Seeding**: Populate the database with sample users, conversations, and messages.  

---

## Tech Stack
- **Backend**: Django 5.2.6, Django REST Framework  
- **Authentication**: djangorestframework-simplejwt  
- **Database**: SQLite (default; can be switched to PostgreSQL/MySQL)  
- **Environment**: django-environ  
- **Python**: 3.13.7  
- **OS**: Windows (tested), Linux/Mac compatible  

---

## Setup Instructions  

### Clone the Repository
```bash
git clone https://github.com/PAULTYLER192/alx-backend-python.git
cd alx-backend-python/messaging_app
```

### Set Up Virtual Environment
```bash
python -m venv venv
.env\Scriptsctivate  # Windows
source venv/bin/activate # Linux/Mac
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Set Up Environment Variables
1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Update `.env` with:
   - A secure `SECRET_KEY`  
   - Your database configuration (if not using SQLite)  
   - Any other sensitive values  

⚠️ **Never commit your `.env` file.** It’s already included in `.gitignore`.  

### Apply Migrations
```bash
python manage.py migrate
```

### Create Superuser
```bash
python manage.py createsuperuser
```

### Run Server
```bash
python manage.py runserver
```

- Admin panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)  
- API root: [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)  

---

## Database Seeding
Populate the database with sample users, conversations, and messages:  
```bash
python manage.py seed
```

- Creates 3 users (demo accounts).  
- Creates 3 conversations with 2–3 random participants.  
- Adds 2–5 messages per conversation.  

Verify in shell:
```python
from chats.models import Conversation, Message
print(Conversation.objects.count())
print(Message.objects.count())
```

---

## API Endpoints  

### Authentication
All endpoints require JWT authentication for write operations (`POST`, `PUT`, `DELETE`).  

**Obtain JWT Tokens**
```powershell
$response = Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/token/" `
    -Method Post `
    -ContentType "application/json" `
    -Body '{"username":"<your_username>","password":"<your_password>"}'

$accessToken = $response.access
Write-Output "Access Token: $accessToken"
```

**Refresh Access Token**
```powershell
$response = Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/token/refresh/" `
    -Method Post `
    -ContentType "application/json" `
    -Body '{"refresh":"<your_refresh_token>"}'
$accessToken = $response.access
```

---

### Conversations
**List or Create**
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/chats/conversations/" `
    -Method Get `
    -Headers @{Authorization = "Bearer $accessToken"}
```

**Create with participants**
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/chats/conversations/" `
    -Method Post `
    -Headers @{Authorization = "Bearer $accessToken"} `
    -ContentType "application/json" `
    -Body '{"participant_ids":[2]}'
```

---

### Messages
**List or Create**
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/chats/messages/" `
    -Method Post `
    -Headers @{Authorization = "Bearer $accessToken"} `
    -ContentType "application/json" `
    -Body '{"conversation_id":1,"content":"Hello, how are you?"}'
```

---

## Troubleshooting  

- **Token Not Valid**:  
  Ensure you’re using the **access token**, not the refresh token. Refresh if expired.  

- **User Not Found**:  
  Verify users exist:
  ```python
  from django.contrib.auth.models import User
  print(User.objects.all())
  ```

- **Permission Denied**:  
  Confirm `REST_FRAMEWORK` in `settings.py` includes `JWTAuthentication`.  

- **Init File Errors**:  
  Ensure `chats/management/__init__.py` and `chats/management/commands/__init__.py` are empty UTF-8 files:
  ```powershell
  Set-Content -Path chats\management\__init__.py -Value "" -Encoding UTF8
  Set-Content -Path chats\management\commands\__init__.py -Value "" -Encoding UTF8
  ```

---

## Contributing
1. Fork the repository.  
2. Create a feature branch:  
   ```bash
   git checkout -b feature/your-feature
   ```  
3. Commit changes:  
   ```bash
   git commit -m "Add your feature"
   ```  
4. Push to the branch:  
   ```bash
   git push origin feature/your-feature
   ```  
5. Open a pull request.  

---

## License  
MIT License  
