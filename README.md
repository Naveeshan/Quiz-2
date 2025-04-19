# Employee Data Generator & Analytics API

A Django-based project that generates synthetic employee data, stores it in Mysql, exposes REST APIs, and provides data visualizations.

## Tech Stack
- Django & Django REST Framework
- PostgreSQL
- Faker (for data generation)
- Swagger (drf-yasg)
- Chart.js or Plotly (optional frontend)
- Docker (optional)

## Features
- Generate employee and performance records.
- REST APIs with filtering and pagination.
- API authentication (Token-based).
- Throttling for rate limiting.
- Swagger UI for interactive documentation.

## Setup Instructions

### Prerequisites
- Python 3.8+
- Mysql Workbench installed

### Installation

```bash
git clone https://github.com/yourusername/employee-analytics
cd employee-analytics
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Configure Database
Set your database credentials in `.env` or `settings.py`:

```env
DB_NAME=employee_db
DB_USER=your_user
DB_PASSWORD=your_pass
DB_HOST=localhost
```

### Migrations and Run
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### Populate Fake Data
```bash
python manage.py generate_employees
```

### API Documentation
Visit [http://localhost:8000/swagger/](http://localhost:8000/swagger/)

---

## Project Structure

```
├── employee/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── analytics/
│   ├── charts/
│   └── views/
├── manage.py
├── requirements.txt
├── README.md
└── design_decisions.md
```

---

## Endpoints Example

- `/api/employees/` — List employees
- `/api/department/` — List departments
- `/api/attendance/` — List attendance
- `/api/performance/` — List performance

---


## Testing

```bash
python manage.py test
```

---

##  Author

- [Your Name](https://github.com/yourusername)
