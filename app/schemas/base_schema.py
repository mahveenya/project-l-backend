from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    @classmethod
    def from_orm_obj(cls, obj):
        return cls.model_validate(obj)

    @classmethod
    def from_orm_list(cls, objs):
        return [cls.model_validate(o) for o in objs]
