from ..db_base import Base

from sqlalchemy import Integer, String, Boolean, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

"""
    id_unit INTEGER NOT NULL REFERENCES units(id_unit),
    id_program INTEGER NOT NULL REFERENCES programs(id_program),
    id_date INTEGER NOT NULL REFERENCES dates(id_date),
    id_sex INTEGER NOT NULL REFERENCES sexes(id_sex),
    concepts VARCHAR(128) NOT NULL,
    numerical_data INTEGER NOT NULL,
    modified_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id_unit, id_program, id_date, id_sex, concepts)
);
"""

class Titulado(Base):
    __tablename__ = "titulados"

    id_unit: Mapped[int] = mapped_column(ForeignKey("units.id_unit"), primary_key=True) 
    id_program: Mapped[int] = mapped_column(ForeignKey("programs.id_program"), primary_key=True)
    id_date: Mapped[int] = mapped_column(ForeignKey("dates.id_date"), primary_key=True) 
    id_sex: Mapped[int] = mapped_column(ForeignKey("sexes.id_sex"), primary_key=True) 
    concepts: Mapped[str] = mapped_column(Integer, nullable=False)
    numerical_data: Mapped[int] = mapped_column(String(128), nullable=False)
    modified_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
