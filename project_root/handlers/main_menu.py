from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery

from project_root import keyboards

router = Router()

@router.message(CommandStart)
async def show_menu(message: Message):
    keyboard = keyboards.main_menu_keyboard()
    await message.answer(text="Главное меню", reply_markup=keyboard)

@router.callback_query(F.data == "main_menu")
async def show_menu(callback_data: CallbackQuery):
    keyboard = keyboards.main_menu_keyboard()
    await callback_data.message.edit_text(text="Главное меню", reply_markup=keyboard)
