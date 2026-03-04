from pydantic import BaseModel


class NamedAPIResource(BaseModel):
    name: str
    url: str


class Effect(BaseModel):
    effect: str
    short_effect: str
    language: NamedAPIResource


class AbilityPokemon(BaseModel):
    pokemon: NamedAPIResource


class Ability(BaseModel):
    id: int
    name: str
    effect_entries: list[Effect]
    pokemon: list[AbilityPokemon]


class AbilityInfo(BaseModel):
    ability: NamedAPIResource


class Pokemon(BaseModel):
    id: int
    name: str
    abilities: list[AbilityInfo]


class PokemonList(BaseModel):
    count: int
    next: str | None
    previous: str | None
    results: list[NamedAPIResource]
