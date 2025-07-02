# Student Management System

A comprehensive Django-based Student Management System for educational institutions to track student performance, courses, subjects, quizzes, and behavior.

## Project Structure

```
myproject/
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── db.sqlite3            # SQLite database
├── myproject/            # Main project directory
│   ├── __init__.py
│   ├── settings.py       # Project settings
│   ├── urls.py          # Main URL configuration
│   ├── wsgi.py          # WSGI configuration
│   └── asgi.py          # ASGI configuration
└── myapp/               # Student Management app
    ├── __init__.py
    ├── admin.py         # Admin configuration
    ├── apps.py          # App configuration
    ├── models.py        # Database models
    ├── views.py         # View functions
    ├── urls.py          # App URL configuration
    ├── tests.py         # Test cases
    └── migrations/      # Database migrations
```

## Features

- **Student Management**: Track student information, ID cards, ranks, and total degrees
- **Course Management**: Manage courses assigned to students
- **Subject Tracking**: Record subjects with full degrees, passing degrees, and earned degrees
- **Quiz Management**: Create and grade quizzes for each course
- **Behavior Monitoring**: Track student behavior as part of the overall grading system
- **Automatic Grade Calculation**: System automatically calculates total degrees based on subjects, quizzes, and behavior

## Database Schema

The system uses the following database structure:

- **Admin**: System administrators
- **Student**: Student records with ID cards, ranks, and total degrees
- **Courses**: Course information linked to students
- **Subjects**: Subject records with grading information
- **Quizzes**: Quiz records with grading information
- **Behavior**: Behavior records with grading information

## Getting Started

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

3. **Create a superuser (if needed):**
   ```bash
   python manage.py createsuperuser
   ```

4. **Start the development server:**
   ```bash
   python manage.py runserver 0.0.0.0:12000
   ```

5. **Access the application:**
   - Main page: http://localhost:12000/
   - Students list: http://localhost:12000/students/
   - Courses list: http://localhost:12000/courses/
   - Admin panel: http://localhost:12000/admin/

## Admin Access

- URL: `/admin/`
- Username: admin
- Password: admin123

## Views

- **Home**: Dashboard with system statistics
- **Students**: List of all students with their details
- **Courses**: List of all courses with their details
- **About**: Information about the system

## Technical Implementation

- Built with Django 5.2.3
- Uses Django signals to automatically update student total degrees
- Implements foreign key relationships between models
- Provides a clean admin interface for data management

## Development

- Add new models in `myapp/models.py`
- Create new views in `myapp/views.py`
- Add URL patterns in `myapp/urls.py`
- Create templates in `myapp/templates/`
- Add static files in `myapp/static/`

## Next Steps

1. Add user authentication and permissions
2. Create detailed student profile pages
3. Implement reporting and analytics
4. Add file upload for student documents
5. Create a REST API for mobile applications