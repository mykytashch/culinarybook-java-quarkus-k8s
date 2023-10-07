
#### Аутентификация и Учетные Записи:
1. `POST /api/auth/register` - Регистрация нового пользователя.
2. `POST /api/auth/login` - Вход в учетную запись пользователя.
3. `GET /api/auth/logout` - Выход из учетной записи пользователя.
4. `GET /api/auth/user` - Получение данных текущего пользователя.
5. `PUT /api/auth/user` - Обновление данных текущего пользователя.
6. `POST /api/auth/forgot-password` - Запрос на сброс пароля.
7. `POST /api/auth/reset-password` - Сброс пароля пользователя.

#### Работа с Рецептами:
8. `GET /api/recipes` - Получение списка всех рецептов.
9. `POST /api/recipes` - Создание нового рецепта.
10. `GET /api/recipes/{recipeId}` - Получение данных конкретного рецепта.
11. `PUT /api/recipes/{recipeId}` - Обновление данных конкретного рецепта.
12. `DELETE /api/recipes/{recipeId}` - Удаление рецепта.
13. `GET /api/recipes/{recipeId}/comments` - Получение комментариев к рецепту.
14. `POST /api/recipes/{recipeId}/comments` - Добавление комментария к рецепту.
15. `GET /api/recipes/{recipeId}/ratings` - Получение рейтинга рецепта.
16. `POST /api/recipes/{recipeId}/ratings` - Установка рейтинга рецепту.
17. `GET /api/recipes/{recipeId}/ingredients` - Получение списка ингредиентов рецепта.
18. `POST /api/recipes/{recipeId}/ingredients` - Добавление ингредиента к рецепту.
19. `PUT /api/recipes/{recipeId}/ingredients/{ingredientId}` - Обновление ингредиента рецепта.
20. `DELETE /api/recipes/{recipeId}/ingredients/{ingredientId}` - Удаление ингредиента рецепта.

#### Личный Кабинет и Социальные Функции:
21. `GET /api/user/{userId}` - Получение данных пользователя по его идентификатору.
22. `PUT /api/user/{userId}` - Обновление данных пользователя.
23. `GET /api/user/{userId}/recipes` - Получение списка рецептов пользователя.
24. `GET /api/user/{userId}/followers` - Получение списка подписчиков пользователя.
25. `GET /api/user/{userId}/following` - Получение списка пользователей, на которых подписан текущий пользователь.
26. `POST /api/user/{userId}/follow` - Подписка на пользователя.
27. `DELETE /api/user/{userId}/unfollow` - Отписка от пользователя.

#### Сообщества и Социальные Функции:
28. `GET /api/communities` - Получение списка сообществ.
29. `GET /api/communities/{communityId}` - Получение данных конкретного сообщества.
30. `POST /api/communities` - Создание нового сообщества.
31. `PUT /api/communities/{communityId}` - Обновление данных сообщества.
32. `DELETE /api/communities/{communityId}` - Удаление сообщества.
33. `GET /api/communities/{communityId}/members` - Получение списка участников сообщества.
34. `POST /api/communities/{communityId}/join` - Присоединение к сообществу.
35. `DELETE /api/communities/{communityId}/leave` - Покидание сообщества.
36. `GET /api/communities/{communityId}/recipes` - Получение рецептов, связанных с сообществом.
37. `POST /api/communities/{communityId}/recipes` - Добавление рецепта к сообществу.
38. `GET /api/communities/{communityId}/events` - Получение событий сообщества (мероприятий и конкурсов).
39. `POST /api/communities/{communityId}/events` - Создание события сообщества.
40. `PUT /api/communities/{communityId}/events/{eventId}` - Обновление данных события сообщества.
41. `DELETE /api/communities/{communityId}/events/{eventId}` - Удаление события сообщества.
42. `POST /api/communities/{communityId}/events/{eventId}/participate` - Участие в событии сообщества.
43. `DELETE /api/communities/{communityId}/events/{eventId}/cancel-participation` - Отмена участия в событии сообщества.

#### Уведомления и Рассылки:
44. `GET /api/notifications` - Получение уведомлений текущего пользователя.
45. `PUT /api/notifications/mark-as-read` - Пометка уведомлений как прочитанных.
46. `POST /api/newsletter/subscribe` - Подписка на информационную рассылку.
47. `POST /api/newsletter/unsubscribe` - Отписка от информационной рассылки.

#### Администрирование и Модерация:
48. `GET /api/admin/users` - Получение списка пользователей (только для администраторов).
49. `PUT /api/admin/users/{userId}` - Обновление данных пользователя (только для администраторов).
50. `DELETE /api/admin/users/{userId}` - Удаление пользователя (только для администраторов).
51. `GET /api/admin/recipes` - Получение списка рецептов (только для администраторов).
52. `PUT /api/admin/recipes/{recipeId}` - Обновление данных рецепта (только для администраторов).
53. `DELETE /api/admin/recipes/{recipeId}` - Удаление рецепта (только для администраторов).
54. `GET /api/admin/comments` - Получение списка комментариев (только для администраторов).
55. `PUT /api/admin/comments/{commentId}` - Обновление данных комментария (только для администраторов).
56. `DELETE /api/admin/comments/{commentId}` - Удаление комментария (только для администраторов).
57. `GET /api/admin/communities` - Получение списка сообществ (только для администраторов).
58. `PUT /api/admin/communities/{communityId}` - Обновление данных сообщества (только для администраторов).
59. `DELETE /api/admin/communities/{communityId}` - Удаление сообщества (только для администраторов).
60. `GET /api/admin/events` - Получение списка событий сообществ (только для администраторов).
61. `PUT /api/admin/events/{eventId}` - Обновление данных события сообщества (только для администраторов).
62. `DELETE /api/admin/events/{eventId}` - Удаление события сообщества (только для администраторов).
