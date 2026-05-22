import uuid
from sqlalchemy import String, DateTime, Boolean, func
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.dialects.postgresql import UUID
from src.app.db.base import Base
from src.app.db.mixins import TimestampMixin


class User(TimestampMixin, Base):
    __tablename__ = "users"

    id = Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid = True),
        primary_key = True,
        default=uuid.uuid4
    )

    email = Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False
    )

    name = Mapped[str] = mapped_column(
        String(255),
        unique = True,
        index = True,
        nullable= False
    )

    hashed_password = Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    is_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )
