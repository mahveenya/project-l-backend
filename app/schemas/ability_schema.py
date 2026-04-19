from app.constants import ResourceTypes
from app.schemas.base_schema import BaseSchema
from app.schemas.common import NamedAPIResourceSchema
from app.schemas.effect_schema import EffectSchema


class AbilityNamedAPIResourceSchema(NamedAPIResourceSchema):
    @classmethod
    def get_resource_type(cls):
        return ResourceTypes.ABILITY

    @classmethod
    def from_model(cls, model, base_url):
        return super().from_model(model, base_url)


class AbilitySchema(BaseSchema):
    id: int
    name: str
    effect_entries: list[EffectSchema]


class AbilityInfoSchema(BaseSchema):
    ability: AbilityNamedAPIResourceSchema

    @classmethod
    def from_resources(cls, resources: list[AbilityNamedAPIResourceSchema]):
        return [cls(ability=r) for r in resources]
