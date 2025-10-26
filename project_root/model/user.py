from sqlalchemy import Column, Integer, String, Boolean, BigInteger
from sqlalchemy.orm import relationship

from project_root.model import Base


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    is_admin = Column(Boolean, nullable=False, default=False)

    queue_entries = relationship("QueueEntry", back_populates="user")

