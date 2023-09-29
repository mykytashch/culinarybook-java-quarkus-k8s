# API Documentation

## Аутентификация и Регистрация
- **POST /auth/register**
  - Описание: Регистрация нового пользователя.
  - Тело запроса: `{ "username": string, "email": string, "password": string }`
  - Ответ: `{ "id": number, "username": string, "email": string }`
  
- **POST /auth/login**
  - Описание: Авторизация пользователя.
  - Тело запроса: `{ "username": string, "password": string }`
  - Ответ: `{ "token": string }`

## Пользователи
- **GET /users/:id**
  - Описание: Получение информации о пользователе по ID.
  - Ответ: `{ "id": number, "username": string, "email": string, "recipes": number[] }`

## Рецепты
- **GET /recipes**
  - Описание: Получение списка всех рецептов.
  - Ответ: `[{ "id": number, "title": string, "description": string, "ingredients": string[], "instructions": string[] }]`
  
- **POST /recipes**
  - Описание: Создание нового рецепта.
  - Тело запроса: `{ "title": string, "description": string, "ingredients": string[], "instructions": string[] }`
  - Ответ: `{ "id": number, "title": string, "description": string, "ingredients": string[], "instructions": string[] }`

- **PUT /recipes/:id**
  - Описание: Обновление существующего рецепта.
  - Тело запроса: `{ "title": string, "description": string, "ingredients": string[], "instructions": string[] }`
  - Ответ: `{ "id": number, "title": string, "description": string, "ingredients": string[], "instructions": string[] }`

- **DELETE /recipes/:id**
  - Описание: Удаление рецепта.
  - Ответ: `{ "message": string }`

