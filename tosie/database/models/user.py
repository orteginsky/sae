from ..db_base import Base
from sqlalchemy import String, Boolean, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id_user: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(128), nullable=False)
    paternal_surname: Mapped[str] = mapped_column(String(128))
    maternal_surname: Mapped[str] = mapped_column(String(128))
    password: Mapped[str] = mapped_column(String(1028), nullable=False)
    id_role: Mapped[int] = mapped_column(ForeignKey("roles.id_role"))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    id_unit: Mapped[int] = mapped_column(ForeignKey("units.id_unit"))
    active: Mapped[bool] = mapped_column(Boolean, default=True)
    modified_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    
