from abc import ABC, abstractmethod

from app.schemas.base_schema import BaseSchema


class LanguageSchema(BaseSchema):
    name: str


class NamedAPIResourceSchema(BaseSchema, ABC):
    name: str
    url: str

    @classmethod
    @abstractmethod
    def get_resource_type(cls) -> str:
        pass

    @classmethod
    def from_model(cls, model):
        return cls(
            name=model.name,
            url=f"/{cls.get_resource_type()}/{model.id}",
        )
