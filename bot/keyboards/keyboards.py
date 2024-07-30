from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup


def get_start_keyboard():
    buttons = [
        [InlineKeyboardButton(text="Подать Школьную", callback_data="post_shk")],
        [InlineKeyboardButton(text="Подать Зиповскую", callback_data="post_zip")],
        [InlineKeyboardButton(text="Отчет PDF", callback_data="get_all_pdf")],
        [InlineKeyboardButton(text="Отчет в сообщении", callback_data="get_all")],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_zip_keyboard():
    buttons = [
        [InlineKeyboardButton(text="Подать Холодную", callback_data="post_zip_cold")],
        [InlineKeyboardButton(text="Подать Горячую", callback_data="post_zip_warm")],
        [InlineKeyboardButton(text="Подать Электричество", callback_data="post_zip_electr")],
        [InlineKeyboardButton(text="Подать все вместе", callback_data="post_zip_all")],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_shk_keyboard():
    buttons = [
        [InlineKeyboardButton(text="Подать Холодную в ванной", callback_data="post_shk_bath_cold")],
        [InlineKeyboardButton(text="Подать Горячую в ванной", callback_data="post_shk_bath_warm")],
        [InlineKeyboardButton(text="Подать Холодную на кухне", callback_data="post_shk_kich_cold")],
        [InlineKeyboardButton(text="Подать Горячую на кухне", callback_data="post_shk_kich_warm")],
        [InlineKeyboardButton(text="Подать электричество", callback_data="post_shk_electr")],
        [InlineKeyboardButton(text="Подать все вместе", callback_data="post_shk_all")],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_report_pdf_keyboard():
    buttons = [
        [InlineKeyboardButton(text="Зиповская", callback_data="get_report_pdf_zip")],
        [InlineKeyboardButton(text="Школьная", callback_data="get_report_pdf_shk")],
        [InlineKeyboardButton(text="Назад", callback_data="back")],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_report_keyboard():
    buttons = [
        [InlineKeyboardButton(text="Зиповская", callback_data="get_report_zip")],
        [InlineKeyboardButton(text="Школьная", callback_data="get_report_shk")],
        [InlineKeyboardButton(text="Назад", callback_data="back")],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_cancel_btn():
    buttons = [
        [KeyboardButton(text="Отмена")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=buttons)
    return keyboard


def get_back_btn():
    buttons = [
        [KeyboardButton(text="Назад")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=buttons)
    return keyboard