import os

DATABASE_URL = os.environ["DATABASE_URL"]


class Endpoints:
    POKEMON_LIST = "/pokemon"
    POKEMON_DETAIL = "/pokemon/{id_or_name}"
    ABILITY_DETAIL = "/ability/{id_or_name}"
    HEALTH_CHECK = "/health"


class ResourceTypes:
    POKEMON = "pokemon"
    ABILITY = "ability"
