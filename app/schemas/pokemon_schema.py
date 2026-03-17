from app.schemas.ability_schema import AbilityInfoSchema
from app.schemas.base_schema import BaseSchema
from app.schemas.common import NamedAPIResourceSchema


class PokemonSchema(BaseSchema):
    id: int
    name: str
    abilities: list[AbilityInfoSchema]


class PokemonListSchema(BaseSchema):
    count: int
    next: str | None
    previous: str | None
    results: list[NamedAPIResourceSchema] = []
