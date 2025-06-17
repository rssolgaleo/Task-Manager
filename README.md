### Hexlet tests and linter status:
[![Actions Status](https://github.com/rssolgaleo/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/rssolgaleo/python-project-52/actions)

[![SonarQube](https://sonarcloud.io/summary/new_code?id=rssolgaleo_python-project-52)]

[![Демонстрация](https://img.shields.io/badge/Веб--приложение-🔗-blue)](https://python-project-52-tt0j.onrender.com/)

# Менеджер задач
Это учебное веб-приложение на Django, реализующее базовый функционал системы управления задачами.  
Позволяет создавать задачи, назначать исполнителей, задавать статусы и метки, а также фильтровать задачи по различным параметрам.

---

## Возможности

- Регистрация и аутентификация пользователей
- CRUD для задач, статусов и меток
- Возможность добавлять несколько меток к задаче
- Только автор задачи может её удалить
- Фильтрация задач по статусу, исполнителю, автору и меткам
- Поддержка flash-сообщений и перевода интерфейса
- Защита связанных объектов от удаления
- Трекинг ошибок через Rollbar
- Анализ качества кода через SonarQube

---

## Стек технологий

| Категория             | Используемое решение             |
|-----------------------|----------------------------------|
| Язык программирования | Python 3.13                      |
| Веб-фреймворк         | Django                           |
| Шаблоны и стили       | Django templates + Bootstrap 5   |
| Работа с БД           | Django ORM, PostgreSQL           |
| Авторизация           | Django Auth                      |
| Фильтрация            | django-filter                    |
| Тестирование          | Django TestCase (unittest)       |
| Отслеживание ошибок   | Rollbar                          |
| Анализ качества кода  | SonarQube                        |
| Менеджер пакетов      | uv                               |
| Деплой                | Render.com (PaaS)                |

---

## Установка и запуск

```bash
uv sync           # Установка зависимостей
make migrate      # Применение миграций
make run          # Запуск локального сервера
make test         # Прогон тестов
make build        # Сборка и деплой проекта
