from ..db_base import Base

from sqlalchemy import DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

"""
-- Tabla: role_privileges
CREATE TABLE role_privileges (
    id_role INTEGER NOT NULL REFERENCES roles(id_role),
    id_privilege INTEGER NOT NULL REFERENCES privileges(id_privilege),
    modified_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id_role, id_privilege)
);
"""

class RolePrivilege(Base):
    __tablename__ = "role_privileges"

    id_role: Mapped[int] = mapped_column(ForeignKey("roles.id_role"), primary_key=True)
    id_privilege: Mapped[int] = mapped_column(ForeignKey("privileges.id_privilege"), primary_key=True)
    modified_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    
