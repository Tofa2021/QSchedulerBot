from sqlalchemy import select
from sqlalchemy.orm import selectinload

from project_root.database import async_session
from project_root.model.queue import Queue
from project_root.model.queue_entry import QueueEntry
from project_root.model.user import User


async def get_all_queues() -> list[Queue]:
    async with async_session() as session:
        result = await session.execute(select(Queue))
        return result.scalars().all()

async def add_queue(name: str):
    async with async_session() as session:
        new_queue = Queue(name=name)
        session.add(new_queue)
        await session.commit()
        return new_queue

async def get_queue_by_id(queue_id: int) -> Queue | None:
    async with async_session() as session:
        result = await session.execute(select(Queue).where(Queue.id == queue_id))
        queue = result.scalar_one_or_none()
        return queue

async def get_users_in_queue(queue_id: int) -> list[User]:
    async with async_session() as session:
        result = await session.execute(
            select(QueueEntry)
            .where(QueueEntry.queue_id == queue_id)
            .options(selectinload(QueueEntry.user))
        )
        entries = result.scalars().all()
        users = [entry.user for entry in entries if entry.user is not None]
        return users

async def is_enqueued(user_id: int, queue_id: int) -> bool:
    users = await get_users_in_queue(queue_id)
    for user in users:
        if user.id == user_id:
            return True

    return False
