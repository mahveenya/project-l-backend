from sqlalchemy import JSON, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base


class AbilityModel(Base):
    __tablename__ = "ability"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    effect_entries: Mapped[list[dict]] = mapped_column(JSON, nullable=False)

    pokemons = relationship(
        "PokemonModel",
        secondary="pokemon_ability",
        back_populates="abilities",
    )
