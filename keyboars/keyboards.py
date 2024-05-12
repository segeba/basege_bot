from aiogram import types

button1 = types.KeyboardButton(text='/start')
button2 = types.KeyboardButton(text='/stop')
button3 = types.KeyboardButton(text='/user')
button4 = types.KeyboardButton(text='/rand')
button5 = types.KeyboardButton(text='djhfk')
button6 = types.KeyboardButton(text='привет')
button7 = types.KeyboardButton(text='как дела?')
button8 = types.KeyboardButton(text='fox')

keyboardStart = [
    [button1, button2, button5],
    [button8, button3, button4],
    [button6, button7],
]

keyword = types.ReplyKeyboardMarkup(keyboard=keyboardStart, resize_keyboard=True)