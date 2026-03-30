# Pokémon API Backend

A FastAPI backend for a Pokémon data API with async SQLAlchemy and PostgreSQL.

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Tech Stack](#tech-stack)
3. [Project Structure](#project-structure)
4. [Getting Started](#getting-started)
5. [Running with Docker](#running-with-docker)
6. [API Endpoints](#api-endpoints)
7. [Database and Migrations](#database-and-migrations)
8. [Application Flow](#application-flow)
9. [Notes](#notes)

---

## Overview

This repository contains the backend service for a Pokémon API. It exposes REST endpoints for Pokémon data and ability data using FastAPI, async SQLAlchemy, and a PostgreSQL database.

## Tech Stack

- Python 3.12
- FastAPI
- Pydantic
- SQLAlchemy 2.x (async)
- asyncpg
- PostgreSQL
- Alembic
- Uvicorn
- ruff
- pre-commit

## Project Structure

```text
.
├── .github/                   # GitHub workflows and CI configuration
├── alembic/                   # Alembic migration configuration and generated revisions
├── app/                       # Application package
│   ├── db/                    # Database models, base, and session setup
│   │   ├── models/            # SQLAlchemy ORM models
│   │   ├── base.py            # Declarative base class
│   │   └── session.py         # Async database session factory
│   ├── repositories/          # Data access layer for database queries
│   ├── schemas/               # Pydantic response models
│   ├── services/              # Business logic and service composition
│   └── utils/                 # Utility helpers (e.g. pagination)
├── scripts/                   # Container entrypoint and startup scripts
├── .dockerignore              # Docker build ignore rules
├── .gitignore                 # Git ignore rules
├── .pre-commit-config.yaml    # Pre-commit hooks configuration
├── Dockerfile                 # Backend container image build
├── Makefile                   # Convenience commands for compose lifecycle
├── README.md                  # Project documentation
├── alembic.ini                # Alembic configuration
├── pyproject.toml             # Python dependencies and tooling config
└── uv.lock                    # Python dependency lock file
```

## Getting Started

### Prerequisites

- Docker
- Docker Compose
- `make` (optional)

### Start the stack

```bash
make up
```

or directly:

```bash
docker compose up -d --build
```

### Stop the stack

```bash
make down
```

or:

```bash
docker compose down
```

### Restart the stack

```bash
make rebuild
```

## Running with Docker

This repository includes a Docker Compose stack that starts the database and backend together.

- `db` starts PostgreSQL 18
- `db-seed` loads `app/db/seed.sql` into the database after startup
- `backend` builds the FastAPI app image and starts the service on port `8000`

The backend container entrypoint is `scripts/entrypoint.sh`, which runs:

1. `alembic upgrade head`
2. `uvicorn app.main:app --host 0.0.0.0 --port 8000`

## API Endpoints

- `GET /` — list Pokémon with pagination
  - Query params: `offset` (default `0`), `limit` (default `20`)
- `GET /pokemon/{identifier}` — fetch a Pokémon by numeric ID only
- `GET /ability/{ability_id}` — fetch an ability by ID

FastAPI also provides interactive docs at:

- `http://localhost:8000/docs`
- `http://localhost:8000/redoc`

Example requests:

```bash
curl http://localhost:8000/
curl http://localhost:8000/pokemon/1
curl http://localhost:8000/ability/1
```

## Database and Migrations

- Database URL inside containers: `postgresql+asyncpg://admin:admin@db:5432/pokemon_db`
- Migrations are stored in the `alembic/` directory
- `scripts/entrypoint.sh` applies migrations on startup
- Seed data is loaded from `app/db/seed.sql`

## Application Flow

- `app/main.py` defines the FastAPI app and routes.
- `app/db/session.py` creates an async SQLAlchemy engine and session maker.
- `app/db/models/` contains ORM models for Pokémon, abilities, and their relations.
- `app/repositories/` performs database queries.
- `app/services/` maps database models into response schemas.
- `app/schemas/` defines Pydantic models for API responses.

## Notes

- The route `GET /pokemon/{identifier}` currently only supports numeric IDs and rejects text-based search.
- There is no dedicated test suite committed to this repository.
- The project is primarily designed to run inside Docker in its current configuration.
- The repository structure separates models, repositories, services, and schemas for maintainability.
- No frontend or test suite is included in this repository.
