# 🏋️‍♂️ Physical Activity Tracking Application

A full-featured web application built with Django that allows users to track their physical activity and promotes a healthy lifestyle. The application enables adding activities, generating statistics, and social interaction – all within a responsive, clean interface.

## 📌 Features

- ✅ User registration and login (including Google OAuth2)
- 📝 Adding, deleting, and commenting on posts
- 🏃 Adding and managing physical activities (category + duration)
- 📈 Generating charts (bar and pie) using Plotly
- 🔒 Option to set profile as public or private
- ⬆️ Import and export activity data in CSV format
- 🧑‍💼 Admin panel with moderation capabilities
- 🌐 Responsive design (Bootstrap)
- 🔎 Searching and following other users
- ☁️ Ready for deployment on Heroku

## 🛠️ Technologies

- **Backend:** Django 5.2.1, Python
- **Frontend:** Bootstrap 5, Crispy Forms
- **Database:** PostgreSQL (locally and through Heroku Postgres add-on)
- **Testing:** Django test framework, Selenium, unit tests
- **Other:** Plotly, Pandas, Humanfriendly, Django Allauth, Django Extensions

## 💻 Local Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-account/activity_tracker.git
   cd activity_tracker
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Linux/Mac
   ```

3. Install dependencies:
   ```bash
   uv sync
   ```

4. Run database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Open your browser and go to `http://127.0.0.1:8000/`

## 🚀 Deployment

The application is prepared for deployment on the [Heroku](https://heroku.com) platform with the free PostgreSQL add-on.

Basic steps:

```bash
heroku create
heroku addons:create heroku-postgresql:hobby-dev
git push heroku main
heroku run python manage.py migrate
```

Heroku environment detection is implemented using:

```python
if 'DYNO' in os.environ:
    is_heroku = True
```

## 📷 Screenshots

*Screenshots will be added soon. The application features an intuitive user interface with responsive design that adapts to different devices.*

## 👥 User Roles

- **Guest:** Can view public profiles and posts
- **User:** Full functionality – posts, activities, statistics, account settings
- **Administrator:** Can moderate content and view private profiles

## 🧪 Testing

- Manual, unit, and automated tests (Selenium)
- Browsers: Chrome, Firefox, Edge, Safari
- Coverage of functional and non-functional requirements

## 📂 Directory Structure

- `activityTracker/` – main Django application
- `templates/` – HTML templates (MVT)
- `static/` – CSS/JS/Bootstrap
- `tests/` – model and form tests
- `media/csvs/` – uploaded CSV files

## 📚 License and Authors

Project created by **Krystian Stasica**
