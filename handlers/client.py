from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboard import kb_client
from aiogram.types import ReplyKeyboardRemove

async def commands_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Приятного аппетита', reply_markup=kb_client)


async def command_work_time(message: types.Message):
    await bot.send_message(message.from_user.id, '24/7')


async def command_place(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Марашал Казакова 68, к. 1',)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(command_work_time, commands=['Режим_работы'])
    dp.register_message_handler(command_place, commands=['Расположение'])
