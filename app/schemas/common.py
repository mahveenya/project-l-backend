from app.schemas.base_schema import BaseSchema


class LanguageSchema(BaseSchema):
    name: str


class NamedAPIResourceSchema(BaseSchema):
    name: str
    url: str

    @classmethod
    def from_model(cls, model, base_url):
        return cls(
            name=model.name,
            url=f"{base_url}/{model.id}",
        )
