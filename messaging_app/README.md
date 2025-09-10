ALX Backend Python: Messaging App
A Django REST Framework (DRF) backend for a messaging application with JWT authentication.
Table of Contents

Project Overview
Features
Tech Stack
Setup Instructions
API Endpoints
Contributing
License

Project Overview
This project is a backend API for a messaging application, allowing users to authenticate and manage messages/conversations. It uses Django REST Framework with JWT authentication.
Features

JWT Authentication: Secure user authentication using JSON Web Tokens.
More features to be added (e.g., messaging, conversations).

Tech Stack

Backend: Django 5.2.6, Django REST Framework
Authentication: djangorestframework-simplejwt
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
.\venv\Scripts\activate  # Windows


Install Dependencies:
pip install -r requirements.txt


Set Up Environment Variables:

Copy .env.example to .env:copy .env.example .env


Edit .env with a secure SECRET_KEY.


Apply Migrations:
python manage.py migrate


Create Superuser:
python manage.py createsuperuser


Run Server:
python manage.py runserver


Admin panel: http://127.0.0.1:8000/admin/.
API: http://127.0.0.1:8000/api/.



API Endpoints

POST /api/token/: Obtain JWT access and refresh tokens.curl -X POST http://127.0.0.1:8000/api/token/ \
-H "Content-Type: application/json" \
-d '{"username":"airbnb_user","password":"your_password"}'


POST /api/token/refresh/: Refresh access token.curl -X POST http://127.0.0.1:8000/api/token/refresh/ \
-H "Content-Type: application/json" \
-d '{"refresh":"your_refresh_token"}'



Contributing

Fork the repository.
Create a feature branch (git checkout -b feature/your-feature).
Commit changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a pull request.

License
MIT License