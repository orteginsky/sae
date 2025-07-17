from ..db_base import Base

from sqlalchemy import String, DateTime, func
from sqlalchemy.orm  import Mapped, mapped_column
from datetime import datetime

"""-- Tabla: privileges
CREATE TABLE privileges (
    id_privilege SERIAL PRIMARY KEY,
    privilege_name VARCHAR(256) NOT NULL,
    modified_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);"""

class Privilege(Base):
    __tablename__ = "privileges"
    
    id_privilege: Mapped[int] = mapped_column(primary_key=True, index=True)
    privilege_name: Mapped[str] = mapped_column(String(256), nullable=False)
    modified_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    