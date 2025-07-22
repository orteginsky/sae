from ..db_base import Base

from sqlalchemy import Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


class Unit(Base):
    __tablename__ = "units"
    id_unit: Mapped[int] = mapped_column(primary_key=True, index=True)
    unit_name: Mapped[str] = mapped_column(String(512), nullable=False)
    unit_acronym: Mapped[str] = mapped_column(String(128), nullable=False)
    capacity: Mapped[int] = mapped_column(Integer)
    id_entidad_federativa: Mapped[int] = mapped_column(Integer)
    intranet_name: Mapped[str] = mapped_column(String(512))
    id_branch: Mapped[int] = mapped_column(ForeignKey("branches.id_branch"))
    modified_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    