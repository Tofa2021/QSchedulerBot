from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from project_root.model.queue import Queue
from project_root.service.queue_service import is_enqueued


def queues_keyboard(queues : list[Queue]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for queue in queues:
        builder.button(text=queue.name, callback_data=f"queue_{queue.id}")

    builder.adjust(1)

    return builder.as_markup()

def main_menu_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(text="Очереди", callback_data="queues")
    builder.button(text="Опции", callback_data="options")

    builder.adjust(1)

    return builder.as_markup()

async def queue_keyboard(user_id : int, queue_id : int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    if await is_enqueued(user_id, queue_id):
        builder.button(text="Освободить", callback_data=f"dequeue_{queue_id}")
    else:
        builder.button(text="Записаться", callback_data=f"enqueue_{queue_id}")

    builder.button(text="В главное меню", callback_data="main_menu")

    builder.adjust(1)

    return builder.as_markup()

def options_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(text="Изменить имя", callback_data="rename")
    builder.button(text="В главное меню", callback_data="main_menu")

    builder.adjust(1)

    return builder.as_markup()
