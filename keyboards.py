from aiogram import types

button1 = types.KeyboardButton(text='/start')
button2 = types.KeyboardButton(text='/stop')
button3 = types.KeyboardButton(text='/info')
button4 = types.KeyboardButton(text='/user')

keyboardStart = [
    [button1, button2],
    [button3, button4]
]

keyword = types.ReplyKeyboardMarkup(keyboard=keyboardStart, resize_keyboard=True)

