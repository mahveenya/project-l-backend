from app.schemas.base_schema import BaseSchema


class NamedAPIResourceSchema(BaseSchema):
    name: str
    url: str

    @classmethod
    def from_model(cls, model):
        return cls(
            name=model.name,
            url=f"/{model.name}/{model.id}",
        )
