# 🛍️ Django Shop Project

Учебный проект интернет-магазина на Django.
На данном этапе реализованы базовые страницы сайта, маршрутизация и форма обратной связи.

---

## 📘 Содержание

- Описание проекта

- Технологии

- Установка и запуск

- Структура проекта

- Функционал

---

## 📖 Описание проекта

**Django Shop Project** — это базовый шаблон интернет-магазина, включающий:

- Главную страницу

- Страницу с контактной информацией

- Форму обратной связи с валидацией данных

- Использование Bootstrap для стилизации интерфейса

Проект создаётся в учебных целях для практики Django, Git и базовых принципов MVC.

---

## ⚙️ Технологии

Python 3.3

Django 5.2.7

HTML5 / Bootstrap 5.3

SQLite (по умолчанию)

Git + GitFlow

---

## 🚀 Установка и запуск

#Клонирование репозитория

    git clone <repo_url>
    cd django_shop

#Создание и активация виртуального окружения

    python -m venv venv
    venv\Scripts\activate         # Windows

#или

    source venv/bin/activate      # Linux / macOS

#Установка зависимостей

    pip install -r requirements.txt

#Применение миграций

    python manage.py migrate

#Запуск сервера разработки

    python manage.py runserver

---

## 🧱 Структура проекта

    django_shop/
    │
    ├── catalog/
    │   ├── migrations/
    │   ├── templates/
    │   │   └── catalog/
    │   │       ├── home.html
    │   │       └── contacts.html
    │   ├── forms.py
    │   ├── models.py
    │   ├── views.py
    │   ├── urls.py
    │   └── admin.py
    │
    ├── shop_project/
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── asgi.py
    │
    ├── manage.py
    ├── requirements.txt
    └── README.md

---

## 💡 Функционал

    ✅ Главная страница (home.html)
    ✅ Контактная страница (contacts.html)
    ✅ Форма обратной связи с валидацией (FeedbackForm)
    ✅ Обработка формы и сообщение об успешной отправке
    ✅ Стилизация с помощью Bootstrap 5

---

## 🌿 GitFlow

- main — стабильная ветка (релизы)

- develop — основная ветка разработки

- feature/homework_22 — текущая ветка задания

---



## ⚙️ Установка
```bash
    git clone <repo_url>
    cd django_shop
    python -m venv venv
    source venv/bin/activate  # или venv\Scripts\activate на Windows
    pip install -r requirements.txt
    python manage.py runserver