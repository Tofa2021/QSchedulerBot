from sqlalchemy import select

from project_root.database import async_session
from project_root.model.user import User


async def get_all_users() -> list[User]:
    async with async_session() as session:
        result = await session.execute(select(User))
        return result.scalars().all()

async def add_user(name: str, is_admin : bool):
    async with async_session() as session:
        new_user = User(name=name, is_admin=is_admin)
        session.add(new_user)
        await session.commit()
        return new_user

async def get_user_by_id(user_id: int) -> User | None:
    async with async_session() as session:
        result = await session.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        return user