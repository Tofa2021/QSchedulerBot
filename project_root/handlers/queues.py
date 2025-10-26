from datetime import datetime

from aiogram import Router, F
from aiogram.types import CallbackQuery

from project_root import keyboards
from project_root.handlers.main_menu import show_menu
from project_root.service.queue_entry_service import get_users_places_in_queue, add_entry, get_places, remove_entry
from project_root.service.queue_service import get_all_queues, get_queue_by_id, get_users_in_queue, is_enqueued
from project_root.service.user_service import get_user_by_id

router = Router()

@router.callback_query(F.data == "queues")
async def show_queues(callback_data: CallbackQuery):
    queues = await get_all_queues()
    keyboard = keyboards.queues_keyboard(queues)
    await callback_data.message.edit_text("Очереди:", reply_markup=keyboard)

@router.callback_query(F.data.startswith("queue_"))
async def show_queue(callback_data: CallbackQuery):
    user_id = callback_data.from_user.id
    queue_id = int(callback_data.data.split("_")[1])
    queue = await get_queue_by_id(queue_id)
    description = await make_description(queue)
    keyboard = await keyboards.queue_keyboard(user_id, queue_id)
    await callback_data.message.edit_text(text=description, reply_markup=keyboard)

async def make_description(queue) -> str:
    places_users = await get_users_places_in_queue(queue.id)
    description = f"{queue.name}\n"
    if len(places_users) == 0:
        description += "Очередь пуста"
    for place_user in places_users:
        place = place_user[0]
        user_id = int(place_user[1])
        user = await get_user_by_id(user_id)
        description += f"{place}) {user.name}\n"

    return description

@router.callback_query(F.data.startswith("enqueue_"))
async def enqueue(callback_data: CallbackQuery):
    user_id = callback_data.from_user.id
    queue_id = int(callback_data.data.split("_")[1])
    free_place = await find_first_free_place(queue_id)
    await add_entry(user_id, queue_id, free_place, datetime.now())
    await show_menu(callback_data)

async def find_first_free_place(queue_id : int):
    places = await get_places(queue_id)
    if len(places) == 0:
        return 1

    for i in range(1, len(places) + 1):
        if i not in places:
            return i

    return None

@router.callback_query(F.data.startswith("dequeue_"))
async def dequeue(callback_data: CallbackQuery):
    user_id = callback_data.from_user.id
    queue_id = int(callback_data.data.split("_")[1])
    await remove_entry(user_id, queue_id)
    await show_menu(callback_data)
