# 🏋️‍♂️ Aplikacja do Zarządzania Aktywnością Fizyczną

Pełnoprawna aplikacja internetowa napisana w Django, która umożliwia użytkownikom śledzenie swojej aktywności fizycznej oraz promuje zdrowy styl życia. Aplikacja pozwala na dodawanie aktywności, generowanie statystyk oraz interakcję społeczną – wszystko w responsywnym, przejrzystym interfejsie.

## 📌 Funkcjonalności

- ✅ Rejestracja i logowanie użytkowników (również przez Google OAuth2)
- 📝 Dodawanie, usuwanie oraz komentowanie postów
- 🏃 Dodawanie i zarządzanie aktywnościami fizycznymi (kategoria + czas trwania)
- 📈 Generowanie wykresów (słupkowych i kołowych) za pomocą Plotly
- 🔒 Możliwość ustawienia profilu jako publiczny lub prywatny
- ⬆️ Import i eksport danych aktywności w formacie CSV
- 🧑‍💼 Panel administratora z możliwością moderacji
- 🌐 Responsywny design (Bootstrap)
- 🔎 Wyszukiwanie i obserwowanie innych użytkowników
- ☁️ Gotowa do wdrożenia na Heroku

## 🛠️ Technologie

- **Backend:** Django, Python
- **Frontend:** Bootstrap
- **Baza danych:** PostgreSQL (lokalnie i przez dodatek Heroku Postgres)
- **Testowanie:** framework testowy Django, Selenium, testy jednostkowe
- **Inne:** Plotly, Pandas, Humanfriendly, Django Allauth, Mermaid

## 🚀 Wdrożenie

Aplikacja została przygotowana do wdrożenia na platformie [Heroku](https://heroku.com) z darmowym dodatkiem PostgreSQL.

Podstawowe kroki:

```bash
heroku create
heroku addons:create heroku-postgresql:hobby-dev
git push heroku main
heroku run python manage.py migrate
```

Wykrywanie środowiska Heroku realizowane jest za pomocą:

```python
if 'DYNO' in os.environ:
    is_heroku = True
```

## 📷 Zrzuty ekranu

> _Można tutaj dodać screeny logowania, panelu użytkownika, wykresów itd._

## 👥 Role użytkowników

- **Gość:** Może przeglądać publiczne profile i posty
- **Użytkownik:** Pełna funkcjonalność – posty, aktywności, statystyki, ustawienia konta
- **Administrator:** Może moderować treści i przeglądać profile prywatne

## 🧪 Testowanie

- Testy manualne, jednostkowe i automatyczne (Selenium)
- Przeglądarki: Chrome, Firefox, Edge, Safari
- Pokrycie wymagań funkcjonalnych i niefunkcjonalnych

## 📂 Struktura katalogów

- `activityTracker/` – główna aplikacja Django
- `templates/` – szablony HTML (MVT)
- `static/` – CSS/JS/Bootstrap
- `tests/` – testy modeli i formularzy
- `media/csvs/` – przesłane pliki CSV

## 📚 Licencja i autorzy

Projekt stworzony przez **Krystiana Stasicę**

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
