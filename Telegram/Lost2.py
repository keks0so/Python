import telebot
import aiogram
from telegram.ext import *
from requests import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
import datetime
import json




quest = 0

bot = Bot(token = "6225304880:AAEI1G5eatn78d440bzHEh4FKHc2xdpUrss")
dp = Dispatcher(bot)

#клавиатура для вещей
button_techno = KeyboardButton("Техника" + "\N{gear}")
button_konc = KeyboardButton("Канцтовары" + "\N{pencil}")
button_document = KeyboardButton("Документы" + "\N{page facing up}")
button_lichn = KeyboardButton("Личные вещи" + "\N{key}")
button_drugoe = KeyboardButton("Другое" + "\N{speech balloon}")
button_back = KeyboardButton("Назад" + "\N{Leftwards Arrow with Hook}")
keyboard_item = ReplyKeyboardMarkup( one_time_keyboard=True, resize_keyboard=True).add(button_techno, button_konc,  button_document, button_lichn, button_drugoe, button_back)

#клавиатура для выбора потерял/нашёл
button_found = KeyboardButton("Нашёл" + "\N{Left-Pointing Magnifying Glass}")
button_lost = KeyboardButton("Потерял" + "\N{Warning Sign}")
keyboard_choose = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(button_found, button_lost)



#клавиатура старт
button_start = KeyboardButton("/start")
keyboard_start = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_start)

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    global choose
    global item
    global when
    global where
    global photo
    global quest
    global info
    await message.answer("Я бот")
    quest = 0
    choose = ''
    item = ''
    when = ''
    where = ''
    photo = ''
    info = ''
    await message.answer("Вы нашли или потеряли вещь?", reply_markup=keyboard_choose)

@dp.message_handler()
async def kb_answer(message: types.Message):
    global choose
    global item
    global item_discr
    global when
    global where
    global photo
    global quest
    global item_category
    quest = quest + 1

    if (message.text == "Нашёл" + "\N{Left-Pointing Magnifying Glass}") or (message.text == "Потерял" + "\N{Warning Sign}"):
        choose = message.text[:-1]

    if message.text == "Назад" + "\N{Leftwards Arrow with Hook}":
        quest = quest - 2
    
    
    if (quest == 2) and ((message.text == "Техника" + "\N{gear}") or (message.text == "Канцтовары" + "\N{pencil}") or (message.text == "Документы" + "\N{page facing up}") or (message.text == "Личные вещи" + "\N{key}") or (message.text == "Другое" + "\N{speech balloon}")):
        item = message.text[:-1]
    elif (quest == 2) and ((message.text != "Техника" + "\N{gear}") or (message.text != "Канцтовары" + "\N{pencil}") or (message.text != "Документы" + "\N{page facing up}") or (message.text != "Личные вещи" + "\N{key}") or (message.text != "Другое" + "\N{speech balloon}")):
        await message.answer("кнопки")
        quest = quest - 1
        

        
    

    if quest == 0:
        await message.answer("Вы нашли или потеряли вещь?", reply_markup=keyboard_choose)
    if (quest == 1) and (choose == "Потерял"):
        
        await message.answer("Какую именно вещь вы потеряли?", reply_markup=keyboard_item)
    if (quest == 1) and (choose == "Нашёл"):
        
        await message.answer("Какую именно вещь вы нашли?", reply_markup=keyboard_item)

   
        

    if quest == 2:
        item_category = message.text[:-1]
        await message.answer("Опишите её подробнее")
        
        
    if (quest == 3) and (choose == "Нашёл"):
        item_discr = ": " + message.text
        await message.answer("Где вы нашли вещь?")
        
    if (quest == 3) and (choose == "Потерял"):
        quest = quest + 1  

    
        

    


    now = datetime.datetime.now()

    # Format date as string
    when = now.strftime("%d-%m-%Y")
    
    if (quest == 4):
        where = message.text 
        await message.answer("Введите номер вашего студенческого биллета (или ФИО если вы не учащийся)")
    
    if (quest == 5) and (choose == "Нашёл"):
        info = message.text
        info = info.lower()
        await message.answer("Идите в 404 кабинет для сдачи найденной вещи")
        
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        # Step 2: Modify the Python object (add new data)
        new_data = {
            "info": info,
            "category": item_category,
            "discryption": item_discr,
            "where": where,
            "when": when
        }

        # Check if data is a list, if not create a new list with existing data
        if not isinstance(data, list):
            data = [data]

        # Append the new data to the existing list
        data.append(new_data)

        # Step 3: Write the updated Python object back to the JSON file
        with open("data.json", "w", encoding="utf-8") as file:
            # Write the JSON data to the file
            json.dump(data, file, ensure_ascii=False)


        quest = quest + 1


    if (quest == 5) and (choose == "Потерял"):
        info = message.text
        info = info.lower()
        
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        # Step 2: Search for specific information
        search_key = "category"  # The key to search for
        search_value =  item_category # The value to search for

        found_items = [] 
        for item in data:
            if search_key in item and item[search_key] == search_value:
                found_items.append(item)

        if found_items:
            await message.answer("Возможно эти объявления о находке вам подойдут:")
            for item in found_items:
                await message.answer(f"Нашёл {item[item_discr]} в {item[where]} в {item[when]}")
        else:
            await message.answer("К сожелению пока никаких подходящих объявлений нету(")


            
    if (quest == 6) and (choose != '') and (item != ''):
        
        await message.answer("Возможно вы потеряли или нашли ещё что-то", reply_markup = keyboard_start)

        
            
        
        
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)