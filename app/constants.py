import os

DATABASE_URL = os.environ["DATABASE_URL"]


class Endpoints:
    POKEMON_BASE = "/api/v1/pokemon"
    ABILITY_BASE = "/api/v1/ability"
    HEALTH_CHECK = "/api/v1/health"
