from ..db_base import Base

from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class Branch(Base):
    __tablename__ = "branches"

    id_branch: Mapped[int] = mapped_column(primary_key=True, index=True)
    branch_name: Mapped[str] = mapped_column(String(128), nullable=False)
    acronym_branch: Mapped[str] = mapped_column(String(64), nullable=False)
    modified_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
