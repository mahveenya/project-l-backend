from app.repositories.ability_repository import get_ability_db_model_by_id
from app.schemas.ability_schema import AbilitySchema


async def get_ability_by_id(session, ability_id) -> AbilitySchema | None:
    ability_db_model = await get_ability_db_model_by_id(session, ability_id)
    if not ability_db_model:
        return None

    return AbilitySchema.from_orm_obj(ability_db_model)
