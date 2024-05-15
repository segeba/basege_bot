from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboars.career_keyboard import make_keyboard


router = Router()


available_jobs = [
    'Программист',
    'Маркетолог',
    'Менеджер',
    'Аналитик',
    'Бухгалтер'
]

available_grades = [
    'Низкий',
    'Средний',
    'Высокий'
]


class Choice(StatesGroup):
    job = State()
    grade = State()


@router.message(F.text.lower() == 'хочу работу')
async def start(message: types.Message, state: FSMContext):
    await message.answer('Какая профессия вас интересует?', reply_markup=make_keyboard(available_jobs))
    await state.set_state(Choice.job)


@router.message(Choice.job, F.text.in_(available_jobs))
async def jobs(message: types.Message, state: FSMContext):
    await message.answer(f'{message.chat.first_name}, Оцените ваш уровень по профессии "{message.text}"',
                         reply_markup=make_keyboard(available_grades))
    await state.set_state(Choice.grade)


@router.message(Choice.job)
async def job_incorrectly(message: types.Message):
    await message.answer('Неправильно. Попробуйте ещё раз', reply_markup=make_keyboard(available_jobs))


@router.message(Choice.grade, F.text.in_(available_grades))
async def grade(message: types.Message, state: FSMContext):
    await message.answer(f'Вы всё прошли, с вами свяжутся наши hr {message.text}',
                         reply_markup=types.ReplyKeyboardRemove())
    await state.clear()


@router.message(Choice.grade)
async def grade_incorrectly(message: types.Message):
    await message.answer('Неправильно. Попробуйте ещё раз', reply_markup=make_keyboard(available_grades))
