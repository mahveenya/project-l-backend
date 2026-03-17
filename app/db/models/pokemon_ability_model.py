from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base


class PokemonAbilityModel(Base):
    __tablename__ = "pokemon_ability"

    pokemon_id: Mapped[int] = mapped_column(
        ForeignKey("pokemon.id", ondelete="CASCADE"),
        primary_key=True,
    )

    ability_id: Mapped[int] = mapped_column(
        ForeignKey("ability.id", ondelete="CASCADE"),
        primary_key=True,
    )
