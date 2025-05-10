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

TO DO

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
