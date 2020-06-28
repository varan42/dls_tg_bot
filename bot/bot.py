from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types.message import ContentType

from config import TOKEN
from text_recognizer.tests.try2 import test_filename
# fsdl_text_recognizer_project.lab5.
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply('Привет! (￣▽￣)ノ Я бот, который пытается в распознавание символов на картинке.\nИспользуй /help, чтобы узнать список доступных команд!')


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Отправь мне фото или документ на английском языке (пока), и я пришлю в ответ распознанный текст. \nНу или напиши мне что-нибудь, и я отправлю этот текст тебе в ответ! Ведь всегда приятно общаться с умными людьми")


@dp.message_handler(content_types=[ContentType.PHOTO,ContentType.DOCUMENT])
async def process_help_command(message: types.Message):
    print(message)
    await message.photo[-1].download(str(message['from']['id']) + "|" + str(message.photo[-1]['file_unique_id']) +'.jpg')
    filename = str(message['from']['id']) + "|" + str(message.photo[-1]['file_unique_id']) +'.jpg'
    await bot.send_message(message.from_user.id, "Получил фото или документ. Идет обработка.")
    print(filename)
    await message.reply('Распознанный текст:\n' + str(test_filename(filename)) + "\nИзвините, я только учусь m(_ _)m")

@dp.message_handler()#не распознал
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

if __name__ == '__main__':
    executor.start_polling(dp)