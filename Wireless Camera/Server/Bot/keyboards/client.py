from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
class ComandKeyboard:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    def __init__(self,one_time,*args) -> None:
        self.kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=one_time)
        for b in args:
            self.kb.add(b)

kb = ComandKeyboard(False, '/registerCamera', '/AddCamera')