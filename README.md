# My Django Angular App

This project is a web application built using Django for the backend and Angular for the frontend. It is designed to support a minimum of 10 to 20 users with at least 2 players in a game environment.

## Project Structure

```
my-django-angular-app
├── backend
│   ├── manage.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── .env
│   ├── mysite
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   ├── apps
│   │   ├── core
│   │   ├── players
│   │   └── game
│   └── scripts
│       └── entrypoint.sh
└── frontend
    ├── angular.json
    ├── package.json
    ├── tsconfig.json
    ├── tsconfig.app.json
    └── src
        ├── main.ts
        ├── index.html
        ├── styles.css
        └── app
            ├── app.module.ts
            ├── app.component.ts
            ├── services
            ├── models
            └── components
```

## Backend

The backend is developed using Django, a high-level Python web framework that encourages rapid development and clean, pragmatic design. The backend includes:

- **Django REST Framework** for building APIs.
- **Docker** support for containerization.
- **Environment variables** management through a `.env` file.

## Frontend

The frontend is developed using Angular, a platform for building mobile and desktop web applications. The frontend includes:

- **Components** for different views (lobby, game, player).
- **Services** for handling API requests and game logic.
- **Models** for defining the structure of player data.

## Getting Started

1. Clone the repository.
2. Navigate to the `backend` directory and install the required packages using:
   ```
   pip install -r requirements.txt
   ```
3. Set up the environment variables in the `.env` file.
4. Run the Django server:
   ```
   python manage.py runserver
   ```
5. Navigate to the `frontend` directory and install the Angular dependencies using:
   ```
   npm install
   ```
6. Start the Angular application:
   ```
   ng serve
   ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.

## License

This project is licensed under the MIT License.