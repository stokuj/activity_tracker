# 🏋️‍♂️ Physical Activity Management Web Application

A full-stack Django web application for tracking physical activity and promoting a healthier lifestyle. It provides users with tools to log activities, generate statistics, and interact socially — all wrapped in a clean, responsive interface.

## 📌 Features

- ✅ User registration and login (also via Google OAuth2)
- 📝 Add, delete, and comment on posts
- 🏃 Add and manage physical activities (with categories and duration)
- 📈 Generate charts (bar/pie) of activity statistics using Plotly
- 🔒 Set profiles as public or private
- ⬆️ Import and export activity data via CSV
- 🧑‍💼 Admin panel with moderation privileges
- 🌐 Responsive design (Bootstrap)
- 🔎 Search and follow other users
- ☁️ Deployment-ready for Heroku

## 🛠️ Technologies Used

- **Backend:** Django, Python
- **Frontend:** Bootstrap
- **Database:** PostgreSQL (locally and via Heroku Postgres add-on)
- **Testing:** Django test framework, Selenium, unit tests
- **Others:** Plotly, Pandas, Humanfriendly, Django Allauth, Mermaid

## 🚀 Deployment

This app is designed to be easily deployable on [Heroku](https://heroku.com) using the free-tier PostgreSQL add-on.

Basic steps:

```bash
heroku create
heroku addons:create heroku-postgresql:hobby-dev
git push heroku main
heroku run python manage.py migrate
```

Environment detection (for dynamic DB config) is handled via:

```python
if 'DYNO' in os.environ:
    is_heroku = True
```

## 📷 Screenshots

TO DO

## 👥 User Roles

- **Guest:** Can view public profiles and posts
- **User:** Full access to posts, activities, charts, account settings
- **Admin:** Can moderate posts/comments and view private profiles

## 🧪 Testing

- Manual, unit, and automated tests (via Selenium)
- Tested on Chrome, Firefox, Edge, and Safari
- Functional and non-functional requirements covered

## 📂 Folder Structure

- `activityTracker/` – main Django app
- `templates/` – HTML templates (MVT)
- `static/` – CSS/JS/Bootstrap
- `tests/` – custom unit tests for models and forms
- `media/csvs/` – CSV upload storage

## 📚 License & Credits

Created by **Krystian Stasica**.


_This project was developed using the waterfall model and includes thorough documentation, testing, and deployment instructions._
