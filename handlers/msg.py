from aiogram import Router, types, F


router = Router()


@router.message(F.text)
async def msg(message: types.Message):
    if 'привет' in message.text.lower():
        await message.reply('И вам день добрый!')
    elif 'как дела' in message.text.lower():
        await message.reply('Нормально. А как ваши дела?')
    else:
        await message.reply('Я вас не понимаю!')
