from app.constants import ResourceTypes
from app.schemas.ability_schema import AbilityInfoSchema
from app.schemas.base_schema import BaseSchema
from app.schemas.common import NamedAPIResourceSchema


class PokemonNamedAPIResourceSchema(NamedAPIResourceSchema):
    @classmethod
    def get_resource_type(cls):
        return ResourceTypes.POKEMON

    @classmethod
    def from_model(cls, model):
        return super().from_model(model)


class PokemonSchema(BaseSchema):
    id: int
    name: str
    abilities: list[AbilityInfoSchema]


class PokemonListSchema(BaseSchema):
    count: int
    next: str | None
    previous: str | None
    results: list[PokemonNamedAPIResourceSchema] = []  # noqa: RUF012
