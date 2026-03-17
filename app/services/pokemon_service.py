from app.repositories.ability_repository import get_ability_db_models_by_pokemon_id
from app.repositories.pokemon_repository import (
    count_pokemon_db_models,
    get_pokemon_db_model_by_id,
    get_pokemon_db_models,
)
from app.schemas.ability_schema import AbilityInfoSchema
from app.schemas.common import NamedAPIResourceSchema
from app.schemas.pokemon_schema import PokemonListSchema, PokemonSchema
from app.utils.pagination import build_pagination


BASE_URL = "/pokemon"


async def get_pokemons_list(session, offset, limit) -> PokemonListSchema:
    pokemons = await get_pokemon_db_models(session, offset, limit)
    total = await count_pokemon_db_models(session)

    results = [NamedAPIResourceSchema.from_model(p) for p in pokemons]

    next_url, previous_url = build_pagination(BASE_URL, total, offset, limit)

    return PokemonListSchema(
        count=total,
        next=next_url,
        previous=previous_url,
        results=results,
    )


async def get_pokemon_by_id(session, pokemon_id) -> PokemonSchema | None:
    pokemon = await get_pokemon_db_model_by_id(session, pokemon_id)
    if not pokemon:
        return None

    abilities = await get_ability_db_models_by_pokemon_id(session, pokemon_id)
    abilities_resources = [NamedAPIResourceSchema.from_model(a) for a in abilities]
    abilities_info = AbilityInfoSchema.from_resources(abilities_resources)
    return PokemonSchema(
        id=pokemon_id,
        name=pokemon.name,
        abilities=abilities_info,
    )
