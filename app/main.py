from fastapi import FastAPI, HTTPException
from fastapi.params import Depends

from app.db.session import get_session
from app.schemas.ability_schema import AbilitySchema
from app.schemas.pokemon_schema import PokemonListSchema, PokemonSchema
from app.services.ability_service import get_ability_by_id
from app.services.pokemon_service import get_pokemon_by_id, get_pokemons_list


app = FastAPI()


@app.get("/", response_model=PokemonListSchema)
async def list_pokemons(
    offset: int = 0,
    limit: int = 20,
    session=Depends(get_session),
) -> PokemonListSchema:
    return await get_pokemons_list(session, offset, limit)


@app.get("/pokemon/{identifier}", response_model=PokemonSchema)
async def get_pokemon(
    identifier: str, session=Depends(get_session)
) -> PokemonSchema | None:
    if identifier.isdigit():
        pokemon = await get_pokemon_by_id(session, int(identifier))
        if pokemon is None:
            raise HTTPException(status_code=404, detail="Pokemon not found")
        return pokemon
    else:
        raise HTTPException(
            status_code=400, detail="Search by substring is not implemented yet"
        )


@app.get("/ability/{ability_id}", response_model=AbilitySchema)
async def get_ability(ability_id: int, session=Depends(get_session)) -> AbilitySchema:
    ability = await get_ability_by_id(session, ability_id)
    if ability is None:
        raise HTTPException(status_code=404, detail="Ability not found")
    return ability
