import math
import os
import telebot
import random
from telebot import types

a = -999
b = -999
e = -999

bot = telebot.TeleBot("1606634697:AAHQwxo2ItpZUmVgm7_jBiApG31hHZ1GARI")
	
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text =='/start':
        bot.send_message(message.from_user.id, 'Привет, меня зовут Лена я была создана для решения уравнений (квадратных и не очень)\nсейчас ты должен будешь ввести значения a, b, c\nВот формула (ax^2+bx+c)\nОстальное сделаю я!\nИнструкция: \n/start = Приветствие \n/go = Решение уравниения')
    elif message.text =='/go':
        bot.send_message(message.from_user.id, 'a = ')
        bot.register_next_step_handler(message, aaa)

def aaa(message):
    global a
    while a == -999:
        try:
            a = float(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Вводите цифрами')
    bot.send_message(message.from_user.id, 'b = ')
    bot.register_next_step_handler(message, bbb)

def bbb(message):
    global b
    while b == -999:
        try:
            b = float(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Вводите цифрами')
    bot.send_message(message.from_user.id, 'c = ')
    bot.register_next_step_handler(message, ccc)

def ccc(message):
    global e
    while e == -999:
        try:
            e = float(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Вводите цифрами') 
            #bot.send_message(message.from_user.id, 'Теперь нажми сюда => /go ')
            #bot.register_next_step_handler(message, resh)
            
            #def resh(message):
    global a
    global b
    
    
    if (a != -999) and (b != -999) and (e != -999):

        if a == 0 and b == 0:
            bot.send_message(message.from_user.id,"Проверьте числа которые вы ввели!")
            raise SystemExit(0)
                
        if a == 0:
            Xв = -e/b
            Yв = 0
            bot.send_message(message.from_user.id, "D(y) = &")
            bot.send_message(message.from_user.id, "E(y) = &")
            bot.send_message(message.from_user.id, "X вершина = " + str(Xв))
            bot.send_message(message.from_user.id, "Y вершина = " + str(Yв))
                
            if b < 0:
                bot.send_message(message.from_user.id, "y > 0 при x Э (-&; " + str(Xв) + ")")
                bot.send_message(message.from_user.id, "y < 0 при x Э (" + str(Xв) + "; +&)")
                    
            elif b > 0:
                bot.send_message(message.from_user.id, "y > 0 при x Э (" + str(Xв) + "; +&)")
                bot.send_message(message.from_user.id, "y < 0 при x Э (-&; " + str(Xв) + ")")

        if b == 0:
            x1 = math.sqrt(-e/a)
            x2 = -math.sqrt(-e/a)
            Xв = 0
            Yв = e
            bot.send_message(message.from_user.id, "Нули функции = (" + str(x1) + "; " + str(x2) + ")")
            bot.send_message(message.from_user.id, "X вершина = " + str(Xв))
            bot.send_message(message.from_user.id, "Y вершина = " + str(Yв))

            if a > 0:
                bot.send_message(message.from_user.id, "Ветви функции направлены вверх")
                bot.send_message(message.from_user.id,"y > 0 при x Э (-&; " + str(x1) + ") v (" + str(x2) + "; +&)")
                bot.send_message(message.from_user.id,"y < 0 при x Э (" + str(x1) + "; " + str(x2) + ")")
                bot.send_message(message.from_user.id,"[" + str(Xв) + "; +&) - возрастает")
                bot.send_message(message.from_user.id,"(-&; " + str(Xв) + "] - убывает")
                        
            elif a < 0:
                bot.send_message(message.from_user.id,"Ветви функции направлены вниз")
                bot.send_message(message.from_user.id,"y > 0 при x Э (" + str(x1) + "; " + str(x2) + ")")
                bot.send_message(message.from_user.id,"y < 0 при x Э (-&; " + str(x1) + ") v (" + str(x2) + "; +&)")
                bot.send_message(message.from_user.id,"(-&; " + str(Xв) + "] - возрастает")
                bot.send_message(message.from_user.id,"[" + str(Xв) + "; +&) - убывает")

        if e == 0:
            x1 = -b/a
            x2 = 0
            Xв = -b/(2*a)
            Yв = (a * (Xв ** 2)) + (b * Xв)
            bot.send_message(message.from_user.id,"Нули функции = (" + str(x1) + "; " + str(x2) + ")")
            bot.send_message(message.from_user.id,"X вершина = " + str(Xв))
            bot.send_message(message.from_user.id,"Y вершина = " + str(Yв))

            if a > 0:
                bot.send_message(message.from_user.id,"Ветви функции направлены вверх")
                bot.send_message(message.from_user.id,"y > 0 при x Э (-&; " + str(x1) + ") v (" + str(x2) + "; +&)")
                bot.send_message(message.from_user.id,"y < 0 при x Э (" + str(x1) + "; " + str(x2) + ")")
                bot.send_message(message.from_user.id,"[" + str(Xв) + "; +&) - возрастает")
                bot.send_message(message.from_user.id,"(-&; " + str(Xв) + "] - убывает")
                        
            elif a < 0:
                bot.send_message(message.from_user.id,"Ветви функции направлены вниз")
                bot.send_message(message.from_user.id,"y > 0 при x Э (" + str(x1) + "; " + str(x2) + ")")
                bot.send_message(message.from_user.id,"y < 0 при x Э (-&; " + str(x1) + ") v (" + str(x2) + "; +&)")
                bot.send_message(message.from_user.id,"(-&; " + str(Xв) + "] - возрастает")
                bot.send_message(message.from_user.id,"[" + str(Xв) + "; +&) - убывает")

                #пункт A); Б)
        elif (a < 0) and (a != 0) and (b != 0) and (e != 0):
            Xв = -b/(2*a)
            Yв = (a * (Xв ** 2)) + (b * Xв) + e
            bot.send_message(message.from_user.id,"Ветви вниз")
            bot.send_message(message.from_user.id,"D(y) = &")
            bot.send_message(message.from_user.id,"E(y) = (-&; " + str(Yв) + "]")
            bot.send_message(message.from_user.id,"X вершина = " + str(Xв))
            bot.send_message(message.from_user.id,"Y вершина = " + str(Yв))
            D = (b**2) - ((4 * a) * e)
            bot.send_message(message.from_user.id,"Дискриминант = " + str(D))

                    #пункт Д)
            if D > 0:
                x1 = (-b-math.sqrt(D))/(2*a)
                x2 = (-b+math.sqrt(D))/(2*a)
                bot.send_message(message.from_user.id,"x1 = " + str(x1))
                bot.send_message(message.from_user.id,"x2 = " + str(x2))

            elif D < 0:
                bot.send_message(message.from_user.id,"Нет корней")

            else:
                bot.send_message(message.from_user.id,"x = Xв")
                        
                        #пункт Е)
            if D > 0 and a > 0:
                bot.send_message(message.from_user.id,"y > 0 при x Э (-&; " + str(x1) + ") v (" + str(x2) + "; +&)")
                bot.send_message(message.from_user.id,"y < 0 при x Э (" + str(x1) + "; " + str(x2) + ")")

            elif D > 0 and a < 0:
                bot.send_message(message.from_user.id,"y > 0 при x Э (" + str(x1) + "; " + str(x2) + ")")
                bot.send_message(message.from_user.id,"y < 0 при x Э (-&; " + str(x1) + ") v (" + str(x2) + "; +&)")

            else:
                bot.send_message(message.from_user.id,"y > 0 при x Э (-&; " + str(Xв) + ") v (" + str(Xв) + "; +&)")

                        #пункт Ж)
            if a > 0:
                bot.send_message(message.from_user.id,"(-&; " + str(Xв) + "] - убывает")
                bot.send_message(message.from_user.id,"[" + str(Xв) + "; +&) - возрастает")

            elif  a < 0:
                bot.send_message(message.from_user.id,"(-&; " + str(Xв) + "] - возрастает")
                bot.send_message(message.from_user.id,"[" + str(Xв) + "; +&) - убывает")

            else:
                bot.send_message(message.from_user.id,"ошибка")

        elif (a > 0) and (a != 0) and (b != 0) and (e != 0) :
            Xв = -b/(2*a)
            Yв = (a*(Xв**2))+(b*Xв)+e
            bot.send_message(message.from_user.id,"Ветви вверх")
            bot.send_message(message.from_user.id,"D(y) = &")
            bot.send_message(message.from_user.id,"E(y) = [" + str(Yв) + "; +&)")
            bot.send_message(message.from_user.id,"X вершина = " + str(Xв))
            bot.send_message(message.from_user.id,"Y вершина = " + str(Yв))
            D = (b**2) - ((4 * a) * e)
            bot.send_message(message.from_user.id,"Дискриминант = " + str(D))

                    #пункт Д)
            if D > 0:
                x1 = (-b-math.sqrt(D))/(2*a)
                x2 = (-b+math.sqrt(D))/(2*a)
                bot.send_message(message.from_user.id,"x1 = " + str(x1))
                bot.send_message(message.from_user.id,"x2 = " + str(x2))

            elif D < 0:
                bot.send_message(message.from_user.id,"Нет корней")

            else:
                bot.send_message(message.from_user.id,"x = Xв")
                
                    #пункт Е)
            if D > 0 and a > 0:
                bot.send_message(message.from_user.id,"y > 0 при x Э (-&; " + str(x1) + ") v (" + str(x2) + "; +&)")
                bot.send_message(message.from_user.id,"y < 0 при x Э (" + str(x1) + "; " + str(x2) + ")")

            elif D > 0 and a < 0:
                bot.send_message(message.from_user.id,"y > 0 при x Э (" + str(x1) + "; " + str(x2) + ")")
                bot.send_message(message.from_user.id,"y < 0 при x Э (-&; " + str(x1) + ") v (" + str(x2) + "; +&)")

            else:
                bot.send_message(message.from_user.id,"y > 0 при x Э (-&; " + str(Xв) + ") v (" + str(Xв) + "; +&)")
                
                    
                    #пункт Ж)
            if a > 0:
                bot.send_message(message.from_user.id,"(-&; " + str(Xв) + "] - убывает")
                bot.send_message(message.from_user.id,"[" + str(Xв) + "; +&) - возрастает")

            elif  a < 0:
                bot.send_message(message.from_user.id,"(-&; " + str(Xв) + "] - возрастает")
                bot.send_message(message.from_user.id,"[" + str(Xв) + "; +&) - убывает")

            else:
                bot.send_message(message.from_user.id,"ошибка")
    a = -999
    b = -999
    e = -999
    bot.send_message(message.from_user.id,"Хотите чтобы я посчетал\nещё что-нибудь - нажмите сюда => /go")

bot.polling( none_stop = True, interval = 0 )