from aiogram import Router, F
from aiogram.types import CallbackQuery

from project_root import keyboards

router = Router()

@router.callback_query(F.data == "options")
async def show_options(callback_data: CallbackQuery):
    keyboard = keyboards.options_keyboard()
    await callback_data.message.edit_text(text="Опции", reply_markup=keyboard)
