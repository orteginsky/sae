from ..db_base import Base

from sqlalchemy import String, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

"""
-- Tabla: programs
CREATE TABLE programs (
    id_program SERIAL PRIMARY KEY,
    program_name VARCHAR(512) NOT NULL,
    id_branch INTEGER NOT NULL REFERENCES branches(id_branch),
    id_level INTEGER NOT NULL REFERENCES levels(id_level),
    modified_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
"""

class Program(Base):
    __tablename__ = "programs"

    id_program: Mapped[int] = mapped_column(primary_key=True, index=True)
    program_name: Mapped[str] = mapped_column(String(512), nullable=False)
    id_branch: Mapped[int] = mapped_column(ForeignKey("branches.id_branch")) 
    id_level: Mapped[int] = mapped_column(ForeignKey("levels.id_level")) 
    modified_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())