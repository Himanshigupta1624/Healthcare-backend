# 🏥 Healthcare Backend API

A comprehensive Django REST Framework backend system for healthcare management, featuring secure patient and doctor record management with JWT authentication.

## 🎯 Overview

This Healthcare Backend API provides a secure and scalable solution for managing healthcare data. Built with Django REST Framework, it offers comprehensive CRUD operations for patients and doctors, secure authentication using JWT tokens, and proper data isolation ensuring users can only access their own patient records.

## ✨ Features

- 🔐 **JWT Authentication** - Secure login with access and refresh tokens
- 👥 **User Management** - Registration and authentication system
- 🏥 **Patient Management** - Full CRUD operations for patient records
- 👨‍⚕️ **Doctor Management** - Complete doctor information management
- 🔗 **Patient-Doctor Mapping** - Assign and manage patient-doctor relationships
- 🛡️ **Data Security** - User-specific data isolation and validation
- 📚 **API Documentation** - Interactive Swagger UI documentation
- 🗄️ **PostgreSQL Database** - Robust and scalable database solution
- ⚡ **Admin Interface** - Django admin for easy data management

## 🛠️ Technology Stack

- **Backend Framework**: Django 5.2.4
- **API Framework**: Django REST Framework 3.16.0
- **Database**: PostgreSQL
- **Authentication**: JWT (djangorestframework-simplejwt 5.5.0)
- **Documentation**: drf-spectacular 0.28.0
- **Environment Management**: python-decouple 3.8
- **Database Adapter**: psycopg2-binary 2.9.10

## 📁 Project Structure

```
Healthcare-backend/
├── heathcare/                    # Main Django project
│   ├── heathcare/               # Project settings
│   │   ├── settings.py          # Django configurations
│   │   ├── urls.py              # Main URL routing
│   │   ├── wsgi.py              # WSGI configuration
│   │   └── asgi.py              # ASGI configuration
│   ├── health/                  # Main application
│   │   ├── models.py            # Database models
│   │   ├── views.py             # API views
│   │   ├── serializers.py       # DRF serializers
│   │   ├── urls.py              # App URL routing
│   │   ├── admin.py             # Admin configurations
│   │   └── migrations/          # Database migrations
│   └── manage.py                # Django management script
├── requirements.txt             # Python dependencies
├── .env.sample                  # Environment variables template
├── .gitignore                   # Git ignore rules
└── README.md                    # Project documentation
```

## 🚀 Installation

### Prerequisites

- Python 3.8+
- PostgreSQL 12+
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/Himanshigupta1624/Healthcare-backend.git
cd Healthcare-backend
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Database Setup

1. Create a PostgreSQL database
2. Copy `.env.sample` to `.env`
3. Update database credentials in `.env`

### Step 5: Run Migrations

```bash
cd heathcare
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### Step 7: Start Development Server

```bash
python manage.py runserver
```

## ⚙️ Configuration

### Key Settings

- **JWT Token Lifetime**: Access tokens expire in 60 minutes
- **Refresh Token Lifetime**: Refresh tokens expire in 7 days
- **Database**: PostgreSQL with connection pooling
- **Time Zone**: Asia/Kolkata
- **Authentication**: JWT-based with token blacklisting

## 📚 API Documentation

Interactive API documentation is available at:

- **Swagger UI**: `http://localhost:8000/api/docs/`
- **API Schema**: `http://localhost:8000/api/schema/`
- **Django Admin**: `http://localhost:8000/admin/`

## 🔗 API Endpoints

### Authentication

| Method | Endpoint | Description | Authentication |
|--------|----------|-------------|----------------|
| POST | `/api/auth/register/` | Register new user | None |
| POST | `/api/auth/login/` | User login | None |
| POST | `/api/auth/refresh/` | Refresh access token | None |

### Patient Management

| Method | Endpoint | Description | Authentication |
|--------|----------|-------------|----------------|
| GET | `/api/patients/` | List user's patients | Required |
| POST | `/api/patients/` | Create new patient | Required |
| GET | `/api/patients/{id}/` | Get patient details | Required |
| PUT | `/api/patients/{id}/` | Update patient | Required |
| DELETE | `/api/patients/{id}/` | Delete patient | Required |

### Doctor Management

| Method | Endpoint | Description | Authentication |
|--------|----------|-------------|----------------|
| GET | `/api/doctors/` | List all doctors | Required |
| POST | `/api/doctors/` | Create new doctor | Required |
| GET | `/api/doctors/{id}/` | Get doctor details | Required |
| PUT | `/api/doctors/{id}/` | Update doctor | Required |
| DELETE | `/api/doctors/{id}/` | Delete doctor | Required |

### Patient-Doctor Mapping

| Method | Endpoint | Description | Authentication |
|--------|----------|-------------|----------------|
| GET | `/api/mappings/` | List user's mappings | Required |
| POST | `/api/mappings/` | Assign doctor to patient | Required |
| GET | `/api/mappings/{patient_id}/` | Get patient's doctors | Required |
| DELETE | `/api/mappings/remove/{id}/` | Remove doctor assignment | Required |

## 💡 Usage Examples

### Register a New User

```bash
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword123",
    "password2": "securepassword123",
    "first_name": "John",
    "last_name": "Doe"
  }'
```

### Login and Get JWT Token

```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "securepassword123"
  }'
```

### Create a Patient

```bash
curl -X POST http://localhost:8000/api/patients/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{
    "name": "Jane Smith",
    "age": 30,
    "gender": "F",
    "phone": "1234567890",
    "address": "123 Main St",
    "medical_history": "No known allergies"
  }'
```

### Create a Doctor

```bash
curl -X POST http://localhost:8000/api/doctors/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{
    "name": "Dr. Smith",
    "specialization": "Cardiology",
    "phone": "9876543210",
    "email": "dr.smith@hospital.com"
  }'
```

## 🧪 Testing

### Manual Testing

Use the provided Swagger UI at `http://localhost:8000/api/docs/` for interactive testing.


## 🗄️ Database Schema

### Models Overview

- **User**: Django's built-in user model for authentication
- **Patient**: Patient information linked to users
- **Doctor**: Healthcare provider information
- **PatientDoctorMapping**: Many-to-many relationship between patients and doctors

### Key Relationships

- `Patient` → `User` (ForeignKey): Each patient belongs to a user
- `PatientDoctorMapping` → `Patient` (ForeignKey): Links patients to doctors
- `PatientDoctorMapping` → `Doctor` (ForeignKey): Links doctors to patients

## 🛡️ Security Features

- **JWT Authentication**: Secure token-based authentication
- **User Data Isolation**: Users can only access their own patient data
- **Input Validation**: Comprehensive data validation using DRF serializers
- **Password Security**: Django's built-in password validation
- **Environment Variables**: Sensitive data stored in environment variables
- **Token Blacklisting**: Refresh token rotation and blacklisting


## 🔧 Admin Interface

Access the Django admin at `http://localhost:8000/admin/` to:

- Manage users, patients, and doctors
- View patient-doctor mappings
- Monitor system data
- Perform administrative tasks

**Built with ❤️ using Django REST Framework**
