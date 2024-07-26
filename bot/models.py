import os

from dotenv import load_dotenv

from bot.answer_text_info import HANDLERS_ANSWER

load_dotenv()
bot_token = os.getenv('BOT_TOKEN')


class TelegramKeyboard:
    contact_with_button = "Зв'язатися з нами"
    where_i_can_buy_button = 'Де купити?'
    service_button = "Сервіс"
    tablet_register_button = "Реєстрація планшету"
    demo_zone_reservation_button = 'Запис в демо-зону'
    partnership_button = "Співпраця"
    other_questions_button = "Залишилися запитання?"
    where_i_can_buy_tablet_button = 'Де купити планшет?'
    where_i_can_buy_acc_button = 'Де купити аксесуари до планшету?'
    back_button = 'Назад'


class TelegramBot:
    token = bot_token


class TelegramBotAnswer:
    answer_contact_with_button = HANDLERS_ANSWER.get('contact_with_button')
    answer_where_i_can_buy_button = HANDLERS_ANSWER.get('contact_with_button')  # must be set
    answer_service_button = HANDLERS_ANSWER.get('service_button')
    answer_tablet_register_button = HANDLERS_ANSWER.get('tablet_register_button')
    answer_demo_zone_reservation = HANDLERS_ANSWER.get('demo_zone_reservation')
    answer_partnership = HANDLERS_ANSWER.get('partnership')
    answer_other_questions = HANDLERS_ANSWER.get('other_questions')
    answer_where_i_can_buy_tablet_button = HANDLERS_ANSWER.get('shops_tablets')
    answer_where_i_can_buy_acc_button = HANDLERS_ANSWER.get('shops_acc')
    answer_back_button = HANDLERS_ANSWER.get('back')
    GREETINGS_TEXT = HANDLERS_ANSWER.get('greetings_text')


    @classmethod
    def split_text_for_tg_answer(cls, answer_text: list):
        """
        split text from answer_list
        :param answer_text:
        :return: str line
        """
        return '\n'.join([str(text) for text in answer_text])