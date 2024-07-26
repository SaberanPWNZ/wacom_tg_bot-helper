from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from bot.keyboards import keyboard, buying_place_kb
from bot.models import TelegramKeyboard, TelegramBotAnswer
from aiogram.types import FSInputFile

router = Router(name='main_router')


@router.message(Command(commands=['start'], prefix='/'))
async def start_handler(message: Message):
    """
    answer when bot was started
    :param message:
    """
    answer = TelegramBotAnswer()
    logo_capture = FSInputFile('bot/media/Wacom-logo.jpg')
    user_name = message.from_user.first_name
    await message.answer(f"Привіт, {user_name if user_name else "Друже"}", reply_markup=keyboard)

    await message.answer_photo(photo=logo_capture)
    await message.answer(text=answer.split_text_for_tg_answer(answer_text=answer.GREETINGS_TEXT))


@router.message(F.text == TelegramKeyboard.contact_with_button)
async def contacts_handler(message: Message):
    answer = TelegramBotAnswer()
    await message.answer(text=answer.split_text_for_tg_answer(answer_text=answer.answer_contact_with_button),
                         reply_markup=keyboard)


@router.message(F.text == TelegramKeyboard.where_i_can_buy_button)
async def where_i_can_buy_handler(message: Message):
    answer = TelegramBotAnswer()
    await message.answer(text="обери варіант", reply_markup=buying_place_kb)


@router.message(F.text == TelegramKeyboard.where_i_can_buy_tablet_button)
async def where_i_can_buy_tablet_handler(message: Message):
    answer = TelegramBotAnswer()
    await message.answer(text=answer.split_text_for_tg_answer(answer_text=answer.answer_where_i_can_buy_tablet_button),
                         reply_markup=keyboard)


@router.message(F.text == TelegramKeyboard.where_i_can_buy_acc_button)
async def where_i_can_buy_acc_handler(message: Message):
    answer = TelegramBotAnswer()
    await message.answer(text=answer.split_text_for_tg_answer(answer_text=answer.answer_where_i_can_buy_acc_button),
                         reply_markup=keyboard)


@router.message(F.text == TelegramKeyboard.back_button)
async def back_handler(message: Message):
    answer = TelegramBotAnswer()
    await message.answer(text=answer.split_text_for_tg_answer(answer_text=answer.answer_back_button),
                         reply_markup=keyboard)


@router.message(F.text == TelegramKeyboard.service_button)
async def service_handler(message: Message):
    answer = TelegramBotAnswer()
    await message.answer(text=answer.split_text_for_tg_answer(answer_text=answer.answer_service_button),
                         reply_markup=keyboard)


@router.message(F.text == TelegramKeyboard.tablet_register_button)
async def tablet_regiser_handler(message: Message):
    answer = TelegramBotAnswer()
    await message.answer(text=answer.split_text_for_tg_answer(answer_text=answer.answer_tablet_register_button),
                         reply_markup=keyboard)


@router.message(F.text == TelegramKeyboard.demo_zone_reservation_button)
async def demo_zone_reservation_handler(message: Message):
    answer = TelegramBotAnswer()
    await message.answer(text=answer.split_text_for_tg_answer(answer_text=answer.answer_demo_zone_reservation),
                         reply_markup=keyboard)


@router.message(F.text == TelegramKeyboard.partnership_button)
async def partnership_handler(message: Message):
    answer = TelegramBotAnswer()
    await message.answer(text=answer.split_text_for_tg_answer(answer_text=answer.answer_partnership),
                         reply_markup=keyboard)


@router.message(F.text == TelegramKeyboard.other_questions_button)
async def other_handler(message: Message):
    answer = TelegramBotAnswer()
    await message.answer(text=answer.split_text_for_tg_answer(answer_text=answer.answer_other_questions),
                         reply_markup=keyboard)


@router.message()
async def all_messsages_handler(message: Message):
    await message.answer(text='Оберіть необхідний пункт', reply_markup=keyboard)
