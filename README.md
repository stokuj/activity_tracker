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
```bash
git clone https://github.com/your-account/activity_tracker.git
cd activity_tracker
```

2. Create environment file from template:
```powershell
Copy-Item .env.example .env
```
```bash
cp .env.example .env
```

3. Create PostgreSQL database (name must match `DB_NAME` in `.env`):
```sql
CREATE DATABASE activityDB2;
```

4. Update `.env` with your local PostgreSQL credentials.

5. Install dependencies:
```bash
uv sync
```

6. Run migrations:
```bash
uv run python manage.py migrate
```

7. Start development server:
```bash
uv run python manage.py runserver 127.0.0.1:8000
```

If port `8000` is busy, run on another port, for example:
```bash
uv run python manage.py runserver 127.0.0.1:8001
```

## Environment Variables

The project uses `.env` (loaded from the project root). Start from `.env.example`.

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG`
- `DJANGO_ALLOWED_HOSTS` (comma-separated, e.g. `localhost,127.0.0.1`)
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`

## Database Behavior

The application validates PostgreSQL connection at startup in local mode.
If the database is missing or credentials are invalid, startup fails with `django.db.utils.OperationalError`.

## Tests

```bash
uv run python manage.py test
```
