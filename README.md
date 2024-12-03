# Quiz Website Project

Developed as part of the Hillel Python Pro course, this quiz website leverages Django Rest Framework (DRF) and a robust backend stack including Redis, Celery, and Docker to offer a dynamic and scalable platform for creating and taking quizzes. Featuring asynchronous task management, a PostgreSQL database, and a user-friendly interface, it's designed for a smooth and engaging user experience.

#### Stack:

- [Python](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/)
- [Redis](https://redis.io/)
- [Celery](https://docs.celeryq.dev/en/stable/)
- [Docker](https://www.docker.com/)
- [DRF](https://www.django-rest-framework.org/)
- [Mongo](https://www.mongodb.com/)

## Local Developing

All actions should be executed from the source directory of the project and only after installing all requirements.

1. Firstly, create and activate a new virtual environment:
   ```bash
   python3.12 -m venv ../venv
   source ../venv/bin/activate
   ```
   
2. Install packages:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
   
3. Run project dependencies, migrations, fill the database with the fixture data etc.:
   ```bash
   ./manage.py migrate
   ./manage.py loaddata <path_to_fixture_files>
   ./manage.py runserver 
   ```
   
4. Docker (https://www.docker.com/):
   ```bash
   docker-compose up
   ```
   

