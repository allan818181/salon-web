<h1 align="center">Salon Website (Django + Docker)</h1>

<p align="center"><b>A bilingual (English/Swahili) salon website, containerized with Docker and ready for PostgreSQL.</b></p>

<p align="center">![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-06B6D4?logo=tailwindcss&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white) ![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?logo=gunicorn&logoColor=white)</p>

## Overview

Bilingual English/Swahili salon website built with Django 5 and Tailwind CSS, containerized with Docker Compose and PostgreSQL, served by Gunicorn + WhiteNoise.

## Features

- Pages: home, services, price menu, gallery, join the team, contact
- Full English and Swahili translations (Django i18n, `locale/`)
- Tailwind CSS styling with reusable navbar/footer partials
- Production setup: Dockerfile + docker-compose, Gunicorn, WhiteNoise static files, environment-based settings

## Tech stack

Python · Django · Tailwind CSS · PostgreSQL · Docker · Gunicorn

## Getting started

```bash
docker compose up --build       # http://localhost:8000
```
Or without Docker:

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver      # http://127.0.0.1:8000
```

## Project structure

`config/` settings · `core/` app (models, views, templates) · `locale/` translations · `Dockerfile`, `docker-compose.yml`

---

<p align="center">Built by <a href="https://github.com/allan818181"><b>Allan Muganyizi Deus</b></a> · Full-Stack &amp; DevOps Engineer · Dar es Salaam, Tanzania<br/>
<a href="https://www.linkedin.com/in/allan-deus-4b888631a">LinkedIn</a> · <a href="mailto:allandeus014@gmail.com">Email</a></p>
