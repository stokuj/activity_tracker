# Activity Tracker

A Django web application for tracking physical activity, sharing posts, and generating activity statistics.

## Features

- User registration and authentication (including Google OAuth via `django-allauth`)
- Activity tracking by category and duration
- Social feed with posts, comments, follow/unfollow
- CSV import/export for activities
- Activity reports with Plotly charts
- Profile privacy and account settings

## Tech Stack

- Python 3.10
- Django 5
- PostgreSQL
- uv (dependency and environment management)
- Plotly, Pandas, Crispy Forms

## Prerequisites

- Python 3.10
- PostgreSQL server running locally
- uv installed (`pip install uv`)

## Quick Start (uv)

1. Clone the repository:

2. Create PostgreSQL database (name must match `DB_NAME` in `.env`):
```sql
CREATE DATABASE activityDB;
```

3. Create `.env` with your local PostgreSQL credentials.
Look at `.env.example`

4. Install dependencies:
```bash
uv sync
```

5. Run migrations and run server
```bash
uv run python manage.py migrate
uv run python manage.py runserver
```

## Database Behavior

The application validates PostgreSQL connection at startup in local mode.
If the database is missing or credentials are invalid, startup fails with `django.db.utils.OperationalError`.

## Tests

```bash
uv run python manage.py test
```
