import telebot
import aiogram
from telegram.ext import *
from requests import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


a = 0
b = 0
quest = 0


bot = Bot(token = "Token)")
dp = Dispatcher(bot)

button_A = KeyboardButton("A)")
button_B = KeyboardButton("B)")

keyboard = ReplyKeyboardMarkup(resize_keyboard=True).row(button_A, button_B)

button_start = KeyboardButton("/start")

keyboard_start = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_start)

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    global a
    global b
    global quest
    await message.reply("Давай начнём профтестирование!", reply_markup=keyboard)
    quest = 0
    a = 0
    b = 0
    await message.answer("A) Анализировать алгоритмы, писать код на языках программирования, используя абстрактные понятия\nИли\nB) Настраивать компьютеры, телефонию, сетевые роутеры, подсоединять принтеры, настраивать программы", reply_markup=keyboard)
    



@dp.message_handler()
async def kb_answer(message: types.Message):
    global a
    global b
    global quest
    quest = quest + 1

    if message.text == "A)":
        a = a + 1
    elif message.text == "B)":
        b = b + 1
    if a + b != quest:
        await message.answer("Я конечно не эксперт, но по-моему на кнопки нажимать удобнее")
        quest = quest - 1
    
    if quest == 0:
        await message.answer("A) Анализировать алгоритмы, писать код на языках программирования, используя абстрактные понятия\nИли\nB) Настраивать компьютеры, телефонию, сетевые роутеры, подсоединять принтеры, настраивать программы", reply_markup=keyboard)
    if quest == 1:
        await message.answer("A) Проверять, выдаёт ли программа правильный ответ\nИли\nB) Проверять компьютерную сеть компании на устойчивость к информационным атакам", reply_markup=keyboard)        
    if quest == 2:
        await message.answer("A) Изучать различные методы разработки качаственных приложений\nИли\nB) Обучать сотрудников не попадать в ловушки хакеров", reply_markup=keyboard)
    if quest == 3:
        await message.answer("A) Исследовать поведение людей в социальных сетях, поисковых системах, на сайтах\nИли\nB) Обеспечивать бесперебойную работу корпоративных компьютеров, закупать их и обновлять", reply_markup=keyboard)
    if quest == 4:
        await message.answer("A) Ежедневно работать со шрифтами, фотографиями, цветами\nИли\nB) Ежедневно изучать операционные системы на предмет наличия в них уязвимостей", reply_markup=keyboard)
    if quest == 5:
        await message.answer("A) Делать компанию привлекательной для клиентов\nИли\nB) Защищать компанию от информационных угроз", reply_markup=keyboard)
    if quest == 6:
        await message.answer("A) Постоянно изучать работы современных дизайнеров\nИли\nB) Постоянно изучать новинки компьютерной техники", reply_markup=keyboard)
    if quest == 7:
        await message.answer("A) Создавать новые алгоритмы\nИли\nB) Собирать компьютеры, объединять их в сеть и устанавливать программы", reply_markup=keyboard)
    if quest == 8:
        await message.answer("A) Тестировать программы, написанные другими\nИли\nB) Изучать и подбирать методы защиты данных от хакеров", reply_markup=keyboard)
            
    

    if (a >= 5) and (quest == 9):
        photo = open('Programmer.jpg', 'rb')
        await message.answer_photo(photo, caption='У вас есть способности для обучения на специальности "Програмирование мобильных устройств"!')
        await message.answer("Хотите пройти тест ещё раз?", reply_markup = keyboard_start)
        
    elif (b >= 5) and (quest == 9):
        photo1 = open('Security.jpg', 'rb')
        await message.answer_photo(photo1, caption='Вам замечательной подойдёт такая специальность как "Техническое обеспечение информационной безопасности"!')
        await message.answer("Хотите пройти тест ещё раз?", reply_markup = keyboard_start)
        
    

executor.start_polling(dp)
