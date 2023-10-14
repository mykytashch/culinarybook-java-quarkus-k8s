Конечно, документация — ключевой аспект любого проекта. Вот базовый шаблон документации для вашей системы:

---

# Документация по проекту Mykyta.fun

## Введение

Этот проект включает в себя фронтенд на React и бекенд на Quarkus. Всё это запущено на Debian сервере и управляется с помощью Nginx.

---

## Директории

- Фронтенд: `/var/www/mykyta.fun/`
- Бекенд: `/home/quarkus_user/culinarybook_backend`

---

## Службы и Демоны

### Nginx

Nginx служит как обратный прокси-сервер для фронтенда и бекенда.

**Путь к конфигурационным файлам:**

- Основной: `/etc/nginx/nginx.conf`
- Для сайтов: `/etc/nginx/sites-enabled/`

**Команды для управления:**

```bash
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl status nginx
```

### Quarkus

Quarkus работает в качестве бекенда.

**Команды для управления:**

Зависит от вашего метода деплоя. Если вы используете `systemd`, файл службы можно найти в `/etc/systemd/system/your_quarkus_service_name.service`

```bash
sudo systemctl start your_quarkus_service_name
sudo systemctl stop your_quarkus_service_name
sudo systemctl restart your_quarkus_service_name
sudo systemctl status your_quarkus_service_name
```

---

## Автоматическое Обновление

Для автоматического обновления используются webhooks:

- Фронтенд: `http://85.215.34.82:3001/webhook-frontend`
- Бекенд: `http://85.215.34.82:3001/webhook-backend`

При получении push-уведомления на GitHub, соответствующий webhook активируется и запускает скрипт для обновления.

**Расположение скриптов:**

- Фронтенд: `/path/to/your/update_frontend.sh`
- Бекенд: `/path/to/your/update_backend.sh`

---

## Запуск при загрузке системы

Все службы настроены так, чтобы автоматически запускаться при загрузке системы, без дополнительного управления.

---

Это только начальная точка, и вы можете добавить много другой полезной информации, такой как примеры API-запросов, часто возникающие проблемы и их решения, и так далее.