from aiogram import Router, F
from aiogram.types import CallbackQuery

from project_root.handlers.main_menu import show_menu
from project_root.service import user_service

router = Router()

@router.callback_query(F.data == "add_user")
async def add_user(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    name = callback_query.from_user.full_name
    await user_service.add_user(user_id, name, True)
    await show_menu(callback_query)

