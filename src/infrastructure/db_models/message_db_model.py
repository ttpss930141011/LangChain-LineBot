""" Defines the window database model.
"""

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import JSON, DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.db_models.db_base import Base

if TYPE_CHECKING:
    from src.infrastructure.db_models import WindowsDBModel

if TYPE_CHECKING:
    from src.infrastructure.db_models import WindowsDBModel


class MessagesDBModel(Base):
    __tablename__ = "messages"

    message_id: Mapped[Integer] = mapped_column(
        Integer, primary_key=True, nullable=False, autoincrement=True
    )
    message: Mapped[JSON] = mapped_column(JSON, nullable=False)
    insert_time: Mapped[DateTime] = mapped_column(DateTime, nullable=False, default=datetime.now)
    update_time: Mapped[DateTime] = mapped_column(
        DateTime, nullable=False, default=datetime.now, onupdate=datetime.now
    )

    window_id: Mapped[str] = mapped_column(
        ForeignKey("windows.window_id", ondelete="CASCADE"), nullable=False
    )
    window: Mapped["WindowsDBModel"] = relationship(
        back_populates="messages", uselist=False, lazy=True
    )
