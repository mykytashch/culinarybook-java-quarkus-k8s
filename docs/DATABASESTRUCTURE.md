

### 1. Таблица Пользователей (Users)
```sql
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    date_joined TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    avatar_url VARCHAR(255),
    bio TEXT
);
```

### 2. Таблица Рецептов (Recipes)
```sql
CREATE TABLE Recipes (
    recipe_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users(user_id),
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    image_url VARCHAR(255)
);
```

### 3. Таблица Комментариев (Comments)
```sql
CREATE TABLE Comments (
    comment_id SERIAL PRIMARY KEY,
    recipe_id INTEGER REFERENCES Recipes(recipe_id),
    user_id INTEGER REFERENCES Users(user_id),
    comment_text TEXT NOT NULL,
    date_commented TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

### 4. Таблица Подписок (Follows)
```sql
CREATE TABLE Follows (
    follower_id INTEGER REFERENCES Users(user_id),
    followed_id INTEGER REFERENCES Users(user_id),
    PRIMARY KEY (follower_id, followed_id)
);
```

### 5. Таблица Сообществ (Communities)
```sql
CREATE TABLE Communities (
    community_id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    description TEXT,
    date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    image_url VARCHAR(255)
);
```

### 6. Таблица Участников Сообществ (CommunityMembers)
```sql
CREATE TABLE CommunityMembers (
    community_id INTEGER REFERENCES Communities(community_id),
    user_id INTEGER REFERENCES Users(user_id),
    PRIMARY KEY (community_id, user_id)
);
```

### 7. Таблица Рецептов в Сообществах (CommunityRecipes)
```sql
CREATE TABLE CommunityRecipes (
    community_id INTEGER REFERENCES Communities(community_id),
    recipe_id INTEGER REFERENCES Recipes(recipe_id),
    PRIMARY KEY (community_id, recipe_id)
);
```

### 8. Таблица Событий Сообществ (CommunityEvents)
```sql
CREATE TABLE CommunityEvents (
    event_id SERIAL PRIMARY KEY,
    community_id INTEGER REFERENCES Communities(community_id),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    date_of_event TIMESTAMP NOT NULL,
    image_url VARCHAR(255)
);
```

### 9. Таблица Участников Событий (EventParticipants)
```sql
CREATE TABLE EventParticipants (
    event_id INTEGER REFERENCES CommunityEvents(event_id),
    user_id INTEGER REFERENCES Users(user_id),
    PRIMARY KEY (event_id, user_id)
);
```

### 10. Таблица Уведомлений (Notifications)
```sql
CREATE TABLE Notifications (
    notification_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users(user_id),
    message TEXT NOT NULL,
    date_sent TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    is_read BOOLEAN NOT NULL DEFAULT FALSE
);
```

Эта структура базы данных предоставляет основу для вашего приложения и может быть расширена или модифицирована в соответствии с вашими конкретными требованиями.