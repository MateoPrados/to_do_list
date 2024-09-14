# 📝 To Do List App

## Description
This is a web application built with Django that allows users to manage their tasks through a simple and intuitive interface. Users can register, log in, and authenticate themselves to create personalized to-do lists. Each task can have a name, description, and can be marked as complete. The app is connected to an SQLite3 database to store user data and tasks.

## Features
- 🔐 User login, registration, and authentication
- 📋 Add, view, update, and delete tasks
- ✅ Mark tasks as completed
- 🗄️ SQLite3 database integration

## Setup Instructions

### 1. Clone the repository:
git clone https://github.com/yourusername/to_do_list.git
cd to_do_list

2. Create a virtual environment and activate it:
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
3. Install dependencies:
pip install -r requirements.txt
4. Run the database migrations:
python manage.py migrate
5. Create a superuser to access the admin panel:
python manage.py createsuperuser
6. Run the server:
python manage.py runserver
7. Open your browser and go to:
http://127.0.0.1:8000/

Technologies Used
🐍 Python 3.12.6
🕸️ Django 5.1.1
💾 SQLite3
🖥️ HTML, CSS

