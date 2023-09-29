
culinary-book-monorepo/
│
├── packages/
│   ├── frontend/
│   │   ├── public/
│   │   │   └── index.html
│   │   ├── src/
│   │   │   ├── components/
│   │   │   │   ├── RecipeCard.js
│   │   │   │   ├── Navbar.js
│   │   │   │   └── UserAvatar.js
│   │   │   ├── pages/
│   │   │   │   ├── HomePage.js
│   │   │   │   ├── RecipePage.js
│   │   │   │   ├── ProfilePage.js
│   │   │   │   └── SearchPage.js
│   │   │   ├── App.js
│   │   │   └── index.js
│   │   ├── tests/
│   │   │   ├── e2e/
│   │   │   │   └── app.e2e.js
│   │   │   ├── integration/
│   │   │   │   └── recipe.integration.js
│   │   │   ├── components/
│   │   │   │   ├── RecipeCard.test.js
│   │   │   │   └── Navbar.test.js
│   │   │   └── pages/
│   │   │       ├── HomePage.test.js
│   │   │       └── ProfilePage.test.js
│   │   ├── Dockerfile
│   │   ├── .dockerignore
│   │   ├── package.json
│   │   ├── .env
│   │   ├── .env.example
│   │   └── README.md
│   │
│   ├── backend/
│   │   ├── src/
│   │   │   ├── main/
│   │   │   │   ├── java/
│   │   │   │   │   ├── controller/
│   │   │   │   │   │   ├── RecipeController.java
│   │   │   │   │   │   └── UserController.java
│   │   │   │   │   ├── service/
│   │   │   │   │   │   ├── RecipeService.java
│   │   │   │   │   │   └── UserService.java
│   │   │   │   │   ├── repository/
│   │   │   │   │   │   ├── RecipeRepository.java
│   │   │   │   │   │   └── UserRepository.java
│   │   │   │   │   ├── domain/
│   │   │   │   │   │   ├── Recipe.java
│   │   │   │   │   │   └── User.java
│   │   │   │   │   ├── config/
│   │   │   │   │   │   └── SecurityConfig.java
│   │   │   │   │   └── CulinaryBookApplication.java
│   │   │   │   ├── resources/
│   │   │   │   │   ├── application.properties
│   │   │   │   │   ├── application-dev.properties
│   │   │   │   │   ├── application-prod.properties
│   │   │   │   │   ├── logback.xml
│   │   │   │   │   └── db/
│   │   │   │   │       ├── migration/
│   │   │   │   │       │   └── V1__Initial_migration.sql
│   │   │   │   │       └── seeds/
│   │   │   │   │           └── initial_data.sql
│   │   │   │   └── Dockerfile
│   │   │   └── test/
│   │   │       ├── java/
│   │   │       │   ├── controller/
│   │   │       │   │   ├── RecipeControllerTest.java
│   │   │       │   │   └── UserControllerTest.java
│   │   │       │   └── service/
│   │   │       │       ├── RecipeServiceTest.java
│   │   │       │       └── UserServiceTest.java
│   │   │       └── resources/
│   │   ├── Dockerfile
│   │   ├── .dockerignore
│   │   ├── pom.xml
│   │   └── README.md
│   │
│   └── shared/
│       └── README.md
│
├── kubernetes/
│   ├── deployments/
│   │   ├── frontend-deployment.yaml
│   │   ├── backend-deployment.yaml
│   │   ├── database-deployment.yaml
│   │   └── nginx-deployment.yaml
│   ├── services/
│   │   ├── frontend-service.yaml
│   │   ├── backend-service.yaml
│   │   ├── database-service.yaml
│   │   └── nginx-service.yaml
│   ├── ingress/
│   │   └── ingress.yaml
│   ├── configmaps/
│   │   ├── frontend-configmap.yaml
│   │   └── backend-configmap.yaml
│   ├── secrets/
│   │   ├── database-secrets.yaml
│   │   └── jwt-secrets.yaml
│   ├── persistentvolumeclaims/
│   │   └── database-pvc.yaml
│   └── helm/
│       ├── Chart.yaml
│       ├── values.yaml
│       ├── templates/
│       │   ├── _helpers.tpl
│       │   ├── deployment.yaml
│       │   ├── service.yaml
│       │   └── ingress.yaml
│       └── charts/
│
├── scripts/
│   ├── init-db.sh
│   ├── build-images.sh
│   ├── deploy.sh
│   └── rollback.sh
│
├── docs/
│   ├── API.md
│   ├── ARCHITECTURE.md
│   ├── CONTRIBUTING.md
│   └── USER_GUIDE.md
│
├── .gitlab-ci.yml
├── Jenkinsfile
├── .editorconfig
├── Vagrantfile
├── .gitignore
├── LICENSE
└── README.md
