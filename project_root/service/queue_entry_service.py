from datetime import datetime
from tkinter import Place

from sqlalchemy import select

from project_root.database import async_session
from project_root.model.queue_entry import QueueEntry


async def get_all_entries() -> list[QueueEntry]:
    async with async_session() as session:
        result = await session.execute(select(QueueEntry))
        return result.scalars().all()

async def add_entry(user_id : int, queue_id : int, place : int, timestamp : datetime):
    async with async_session() as session:
        new_entry = QueueEntry(user_id=user_id, queue_id=queue_id, place=place, timestamp=timestamp)
        session.add(new_entry)
        await session.commit()
        return new_entry

async def get_entry_by_id(entry_id: int) -> QueueEntry | None:
    async with async_session() as session:
        result = await session.execute(select(QueueEntry).where(QueueEntry.id == entry_id))
        entry = result.scalar_one_or_none()
        return entry

async def get_places_in_queue(queue_id: int) -> list[tuple[int]]:
    async with async_session() as session:
        result = await session.execute(
            select(QueueEntry.place, QueueEntry.user_id).where(QueueEntry.queue_id == queue_id)
        )
        places_and_users = result.all()
        return places_and_users

