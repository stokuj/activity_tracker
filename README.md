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

- **Backend:** Django 5.2.1, Python
- **Frontend:** Bootstrap 5, Crispy Forms
- **Baza danych:** PostgreSQL (lokalnie i przez dodatek Heroku Postgres)
- **Testowanie:** framework testowy Django, Selenium, testy jednostkowe
- **Inne:** Plotly, Pandas, Humanfriendly, Django Allauth, Django Extensions

## 💻 Instalacja lokalna

1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/twoje-konto/activity_tracker.git
   cd activity_tracker
   ```

2. Utwórz i aktywuj wirtualne środowisko:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Linux/Mac
   ```

3. Zainstaluj zależności:
   ```bash
   pip install -r requirements.txt
   ```

4. Wykonaj migracje bazy danych:
   ```bash
   python manage.py migrate
   ```

5. Uruchom serwer deweloperski:
   ```bash
   python manage.py runserver
   ```

6. Otwórz przeglądarkę i przejdź pod adres `http://127.0.0.1:8000/`

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

*Zrzuty ekranu zostaną dodane wkrótce. Aplikacja posiada intuicyjny interfejs użytkownika z responsywnym designem, który dostosowuje się do różnych urządzeń.*

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

---

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
   pip install -r requirements.txt
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
