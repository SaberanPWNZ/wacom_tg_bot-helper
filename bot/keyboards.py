from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from bot.models import TelegramKeyboard


kb = [[KeyboardButton(text=TelegramKeyboard.contact_with_button),
                              KeyboardButton(text=TelegramKeyboard.where_i_can_buy_button)],
      [KeyboardButton(text=TelegramKeyboard.service_button),
                              KeyboardButton(text=TelegramKeyboard.partnership_button)],
      [KeyboardButton(text=TelegramKeyboard.tablet_register_button),
                              KeyboardButton(text=TelegramKeyboard.demo_zone_reservation_button)],
      [KeyboardButton(text=TelegramKeyboard.other_questions_button)],

]

buying_place_shops = [
      [KeyboardButton(text=TelegramKeyboard.where_i_can_buy_tablet_button)],
      [KeyboardButton(text=TelegramKeyboard.where_i_can_buy_acc_button)],
      [KeyboardButton(text=TelegramKeyboard.back_button)]
]


keyboard = ReplyKeyboardMarkup(keyboard=kb)
buying_place_kb = ReplyKeyboardMarkup(keyboard=buying_place_shops)

