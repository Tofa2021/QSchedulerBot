from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship

from project_root.model import Base


class QueueEntry(Base):
    __tablename__ = 'queue_entries'

    id = Column(Integer, primary_key=True)
    queue_id = Column(Integer, ForeignKey('queues.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    place = Column(Integer, nullable=False)
    timestamp = Column(DateTime, nullable=False)

    __table_args__ = (
        UniqueConstraint('queue_id', 'place', name='unique_queue_place'),
    )

    user = relationship('User', back_populates='queue_entries')
    queue = relationship('Queue', back_populates='entries')