from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def make_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    if len(items) > 3:
        row1 = [KeyboardButton(text=item) for item in items[:3]]
        row2 = [KeyboardButton(text=item) for item in items[3:]]
        keyboard = ReplyKeyboardMarkup(keyboard=[row1, row2], resize_keyboard=True)
        return keyboard
    else:
        row = [KeyboardButton(text=item) for item in items]
        keyboard = ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)
        return keyboard