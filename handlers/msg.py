from aiogram import Router, types, F


router = Router()


@router.message(F.text)
async def msg(message: types.Message):
    if 'привет' in message.text.lower():
        await message.reply('И тебе привет!')
    elif 'как дела' in message.text.lower():
        await message.reply('Нормально. А у тебя как?')
    else:
        await message.reply('Моя твоя не понимать!')
