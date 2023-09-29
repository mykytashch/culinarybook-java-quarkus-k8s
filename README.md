# Culinary Book Monorepo

This monorepo houses the codebase for the Culinary Book project, a personal learning endeavor aimed at honing development skills. It is organized into frontend, backend, and shared packages.

## Technologies Utilized

- **Frontend:**
  - React.js for building the user interface.
  - Docker for containerization.

- **Backend:**
  - Quarkus as the backend framework.
  - Docker for containerization.
  - PostgreSQL for database management.

- **Shared:**
  - Libraries and utilities shared between the frontend and backend.

- **Infrastructure:**
  - Kubernetes for orchestration.
  - Helm for managing Kubernetes packages.

- **Testing:**
  - Jest for frontend testing.
  - JUnit for backend testing.

- **Continuous Integration/Continuous Deployment (CI/CD):**
  - Utilizing GitLab CI and Jenkins for CI/CD pipelines.

- **Documentation:**
  - Markdown files for detailing API, architecture, contribution guidelines, and user guide.

## Significance of Key Technologies

- **Quarkus:**
  Quarkus is a cutting-edge, Kubernetes-native Java framework tailored for Java virtual machines (JVMs) and native compilation, optimizing Java specifically for containers and enabling it to become an effective platform for serverless, cloud, and Kubernetes environments. By learning and implementing Quarkus, not only is the project aligned with modern development standards, but it also explores efficient backend development optimized for cloud deployment.

- **Kubernetes:**
  Kubernetes is a powerful open-source container orchestration system that automates the deployment, scaling, and management of containerized applications. Incorporating Kubernetes provides hands-on experience with a highly sought-after technology in the industry, learning how to manage microservices and containerized applications at scale.

- **Java:**
  Java remains a robust, high-level, class-based, object-oriented programming language with strong memory management, concurrent execution model, and a wealth of libraries. By building the backend with Java, the project delves into creating scalable, maintainable, and efficient backend systems, which are crucial skills for modern software development.

## Project Structure

The project is structured as a monorepo with three main packages: frontend, backend, and shared. Each package has its specific dependencies, Dockerfile for containerization, and README for detailed instructions.

## Getting Started

Refer to the `USER_GUIDE.md` for instructions on setting up the development environment, building, and deploying the project.

## Contributing

As this is a personal learning project, contributions are not open. However, feel free to explore the codebase.

## License

This project is for educational purposes and is not licensed.

## Contact

GitHub Profile: [mykytashch](https://github.com/mykytashch)



Конечно! Вот простая и краткая инструкция-памятка по работе с GitHub:

### Инструкция-памятка по работе с GitHub

1. **Создание новой ветки (branch)**
   - Перед тем как начать новую задачу, убедитесь, что вы находитесь в актуальной версии главной ветки (например, `main` или `master`).
     ```
     git checkout master
     git pull
     ```
   - Создайте новую ветку, где `my-feature` - имя вашей ветки.
     ```
     git checkout -b my-feature
     ```

2. **Работа в ветке**
   - Регулярно сохраняйте свои изменения с помощью коммитов:
     ```
     git add .
     git commit -m "Краткое описание ваших изменений"
     ```

3. **Обновление вашей ветки**
   - Чтобы ваши изменения не конфликтовали с основной веткой, время от времени подтягивайте обновления:
     ```
     git pull origin master
     ```

4. **Отправка изменений на GitHub**
   - Пушьте вашу ветку на GitHub:
     ```
     git push -u origin my-feature
     ```

5. **Создание Pull Request (PR)**
   - Перейдите на GitHub и нажмите кнопку "New Pull Request" в вашей ветке.
   - Убедитесь, что основная ветка выбрана в качестве "base", а ваша ветка — в качестве "compare".
   - Заполните информацию о вашем PR и отправьте его на рассмотрение.

6. **Слияние (merge) вашего PR**
   - После проверки и утверждения вашего PR, выполните слияние в основную ветку.
   - В случае конфликтов, решите их локально или с помощью интерфейса GitHub, а затем завершите слияние.

7. **Закрытие задачи**
   - После успешного слияния вашего PR, убедитесь, что ваша задача/исправление реализовано корректно и закройте связанный с ней issue на GitHub (если он был создан).

Не забудьте регулярно обновлять свои знания и следить за изменениями в инструкциях и лучших практиках работы с Git и GitHub.
