from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from project_root.model import Base


class Queue(Base):
    __tablename__ = "queues"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    entries = relationship("QueueEntry", back_populates="queue")

