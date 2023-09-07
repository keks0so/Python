import math
#import configure
import telebot
import random
from telebot import types

i = 0
p =0
t =0
ch=0
z =0
h=0


bot = telebot.TeleBot('1573212023:AAG6D0RWmDDKKHI7LYVNsF985OYkSVTOazE')

@bot.message_handler(commands = ['info'])
@bot.message_handler(func=lambda m: True)
@bot.message_handler(func=lambda call: True)
def echo_all(message):
    if message.text =='/start':
        bot.send_message(message.from_user.id, 'Привет, сейчас я помогу тебе выбрать профеcсию с помощью небольшого теста.\nВ нём будут представлены разные действия, а твоя задача выбрать то,\nкоторое больше тебе нравится\nОстальное сделаю я!\nИнструкция: \n/start = Приветствие \n/go = Тест')
    if message.text =='/go':
        bot.send_message(message.from_user.id,'И так начнём')
        global i
        global p
        global t
        bot.send_message(message.chat.id,'/A) Ухаживать за животными\nИли\n/B) Обслуживать машины, приборы (следить, регулировать)')
        if message.text == '/A':
            p=p+1
        if message.text == '/B':
            t=t+1
        i=i+1
        bot.register_next_step_handler(message, two)
                        
def two(message):
        global i
        global ch
        global z
        bot.send_message(message.chat.id,'/A) Помогать больным\nИли\n/B) Составлять таблицы, схемы, программы для вычислительных машин')
        if message.text == '/A':
            ch=ch+1
        if message.text == '/B':
            z=z+1
        i=i+1
        bot.register_next_step_handler(message, three)
                        
def three(message):
            global i
            global h
            global p
            bot.send_message(message.chat.id,'/A) Следить за качеством книжных иллюстраций, плакатов, художественных открыток, грампластинок\nИли\n/B) Следить за состоянием, развитием растений')
            if message.text == '/A':
                h=h+1
            if message.text == '/B':
                p=p+1
            i=i+1
            bot.register_next_step_handler(message, four)
                        
def four(message):
            global i
            global t
            global ch
            bot.send_message(message.chat.id,'/A) Обрабатывать материалы (дерево, ткань, металл, пластмассу и т.п.)\nИли\n/B) Доводить Товары до потребителя, рекламировать, продавать')
            if message.text == '/A':
                t=t+1
            if message.text == '/B':
                ch=ch+1
            i=i+1
            bot.register_next_step_handler(message, five)
                        
def five(message):
            global i
            global h
            global z
            bot.send_message(message.chat.id,'/A) Обсуждать научно-популярные книги, статьи\nИли\n/B) Обсуждать художественные книги (или пьесы, концерты)')
            if message.text == '/A':
                z=z+1
            if message.text == '/B':
                h=h+1
            i=i+1
            bot.register_next_step_handler(message, six)

def six(message):
            global i
            global ch
            global p
            bot.send_message(message.chat.id,'/A) Выращивать молодняк (животных какой-либо породы)\nИли\n/B) Тренировать товарищей (или младших) в выполнении каких-либо действий (трудовых, учебных, спортивных)')
            if message.text == '/A':
                p=p+1
            if message.text == '/B':
                ch=ch+1
            i=i+1
            bot.register_next_step_handler(message, seven)

def seven(message):
            global i
            global h
            global t        
            bot.send_message(message.chat.id,'/A) Копировать рисунки, изображения (или настраивать музыкальные инструменты)\nИли\n/B) Управлять каким-либо грузовым (подъемным или транспортным) средством – подъемным краном, трактором, тепловозом и др.')
            if message.text == '/A':
                h=h+1
            if message.text == '/B':
                t=t+1
            i=i+1
            bot.register_next_step_handler(message, eight)
                        
def eight(message):
            global i
            global h
            global ch        
            bot.send_message(message.chat.id,'/A) Сообщать, разъяснять людям нужные им сведения (в справочном бюро, на экскурсии и т.д.)\nИли\n/B) Оформлять выставки, витрины (или участвовать в подготовке пьес, концертов)')
            if message.text == '/A':
                ch=ch+1
            if message.text == '/B':
                h=h+1
            i=i+1
            bot.register_next_step_handler(message, nine)

def nine(message):
            global i
            global t
            global z        
            bot.send_message(message.chat.id,'/A) Ремонтировать вещи, изделия (одежду, технику), жилище\nИли\n/B) Искать и исправлять ошибки в текстах, таблицах, рисунках')
            if message.text == '/A':
                t=t+1
            if message.text == '/B':
                z=z+1
            i=i+1
            bot.register_next_step_handler(message, ten)

def ten(message):
            global i
            global z
            global p        
            bot.send_message(message.chat.id,'/A) Лечить животных\nИли\n/B) Выполнять вычисления, расчеты')
            if message.text == '/A':
                p=p+1
            if message.text == '/B':
                z=z+1
            i=i+1
            bot.register_next_step_handler(message, eleven)

def eleven(message):
            global i
            global t
            global p        
            bot.send_message(message.chat.id,'/A) Выводить новые сорта растений\nИли\n/B) Конструировать, проектировать новые виды промышленных изделий (машины, одежду, дома, продукты питания и т.п.)')
            if message.text == '/A':
                p=p+1
            if message.text == '/B':
                t=t+1
            i=i+1
            bot.register_next_step_handler(message, tvelve)

def tvelve(message):
            global i
            global ch
            global z        
            bot.send_message(message.chat.id,'/A) Разбирать споры, ссоры между людьми, убеждать, разъяснять, наказывать, поощрять\nИли\n/B) Разбираться в чертежах, схемах, таблицах (проверять, уточнять, приводить в порядок)')
            if message.text == '/A':
                ch=ch+1
            if message.text == '/B':
                z=z+1
            i=i+1
            bot.register_next_step_handler(message, thirteen)

def thirteen(message):
            global i
            global h
            global p        
            bot.send_message(message.chat.id,'/A) Наблюдать, изучать работу кружков художественной самодеятельности\nИли\n/B) Наблюдать, изучать жизнь микробов')
            if message.text == '/A':
                h=h+1
            if message.text == '/B':
                p=p+1
            i=i+1
            bot.register_next_step_handler(message, fourteen)
                        
def fourteen(message):
            global i
            global ch
            global t        
            bot.send_message(message.chat.id,'/A) Обслуживать, налаживать медицинские приборы, аппараты\nИли\n/B) Оказывать людям медицинскую помощь при ранениях, ушибах, ожогах и т.п.')
            if message.text == '/A':
                t=t+1
            if message.text == '/B':
                ch=ch+1
            i=i+1
            bot.register_next_step_handler(message, fiveteen)

def fiveteen(message):
            global i
            global h
            global z        
            bot.send_message(message.chat.id,'/A) Составлять точные описания-отчеты о наблюдаемых явлениях, событиях, измеряемых объектах и др.\nИли\n/B) Художественно описывать, изображать события (наблюдаемые и представляемые)')
            if message.text == '/A':
                    z=z+1
            if message.text == '/B':
                h=h+1
            i=i+1
            bot.register_next_step_handler(message, sixteen)

def sixteen(message):
            global i
            global ch
            global p        
            bot.send_message(message.chat.id,'/A) Делать лабораторные анализы в больнице\nИли\n/B) Принимать, осматривать больных, беседовать с ними, назначать лечение')
            if message.text == '/A':
                p=p+1
            if message.text == '/B':
                ch=ch+1
            i=i+1
            bot.register_next_step_handler(message, seventeen)

def seventeen(message):
            global i
            global h
            global t        
            bot.send_message(message.chat.id,'/A) Красить или расписывать стены помещений, поверхность изделий\nИли\n/B) Осуществлять монтаж или сборку машин, приборов')
            if message.text == '/A':
                h=h+1
            if message.text == '/B':
                t=t+1
            i=i+1
            bot.register_next_step_handler(message, eighteen)

def eighteen(message):
            global i
            global h
            global ch        
            bot.send_message(message.chat.id,'/A) Организовать культпоходы сверстников или младших в театры, музеи, экскурсии, туристические походы и т.п.\nИли\n/B) Играть на сцене, принимать участие в концертах')
            if message.text == '/A':
                ch=ch+1
            if message.text == '/B':
                h=h+1
            i=i+1
            bot.register_next_step_handler(message, nineteen)

def nineteen(message):
            global i
            global t
            global z        
            bot.send_message(message.chat.id,'/A) Изготовлять по чертежам детали, изделия (машины, одежду), строить здания\nИли\n/B) Заниматься черчением, копировать чертежи, карты')
            if message.text == '/A':
                t=t+1
            if message.text == '/B':
                z=z+1
            i=i+1
            bot.register_next_step_handler(message, twenty)

def twenty(message):
            global i
            global z
            global p        
            bot.send_message(message.chat.id,'/A) Вести борьбу с болезнями растений, с вредителями леса, сада\nИли\n/B) Работать на клавишных машинах (пишущей машинке, телетайпе, наборной машине и др.)')
            if message.text == '/A':
                p=p+1
            if message.text == '/B':
                z=z+1
            i=i+1
            bot.register_next_step_handler(message, otv)
     
                
    

def otv(message):
    global p
    global t
    global ch
    global z
    global h
    if p >= 4:
        bot.send_message(message.chat.id,'Человек - природа' + '(' + str(p) + '/8)\nВы — друг всего живого на планете Земля! Именно такие как вы становятся исследователями богатого Царства живой природы, создают сотни новых культур растений, лечат и спасают животных. Возможно, в вас закрался и талант первооткрывателя?\nВам могут подойти такие професии как: биолог, агроном, ветеринар, лесник, зоотехник, агрохимик, садовод')
        
    if t>= 4:
        bot.send_message(message.chat.id,'Человек - техника' + '(' + str(t) + '/8)\nТехнический прогресс не стоит на месте и вы — его вечный двигатель! Вы знаете, как управиться со сломанным будильником, сможете точно настроить любую технику, не боитесь по-новому взглянуть на обычные вещи и, прикрутив пару гаек, получить новое изобретение. Сложные механизмы не пугают, а вдохновляют вас. Но вы умеете использовать не только воображение, но и смекалку, чтобы найти общий язык с любой техникой.\nВам могут подойти такие професии как: инженер, конструктор, техник, слесарь, радиомеханик, пилот, электрик')
        
    if ch>= 4:
        bot.send_message(message.chat.id,'Человек - человек' + '(' + str(ch) + '/8)\nВ людском потоке вы как рыба в воде! Постоянный контакт с окружающими вас не пугает, напротив, в каждом человеке вы можете увидеть что-то интересное. Вы с легкостью делитесь своим опытом, умеете договариваться и сопереживать. Как правило, ваша роль — душа компании и на отдыхе, и на работе\nВам могут подойти такие професии как: учитель, воспитатель, спортивный тренер, медицинский работник, сфера обслуживания, экскурсовод, юрист, специалист кадровой службы')
        
    if z>= 4:
        bot.send_message(message.chat.id,'Человек - знаковая система' + '(' + str(z) + '/8)\nЧто уж греха таить, в точных науках вам нет равных! Математические расчеты, статистика, чертежи, информационные технологии… для вас это не просто цифры и графики — это увлекательный мир, полный находок и загадок. Для самого запутанного дела вы без труда создадите удобный план действий. Вы — неоценимый работник там, где требуется внимательность, усидчивость и хорошая память.\nВам могут подойти такие професии как: программист, геодезист, математик, экономист, бухгалтер, редактор, корректор, делопроизводитель')
        
    if h>= 4:
        bot.send_message(message.chat.id,'Человек - художественный образ' + '(' + str(h) + '/8)\nВы созданы для того, чтобы приносить красоту в наш суровый мир! Скорее всего, вы уже давно чувствуете в себе творческую жилку — шила в мешке ведь не утаишь… В любом случае, ваше воображение, интуиция и нестандартный взгляд на окружающих пригодятся в создании чудесных произведений искусства. Будь это музыка, литература, театр, дизайн или архитектура — все вам под силу!\nВам могут подойти такие професии как: актер, писатель, дизайнер, художник-оформитель, композитор, модельер, архитектор, скульптор, флорист, реставратор, гравер, ювелир, журналист, хореограф')
        

    p = 0
    t = 0
    ch = 0
    z = 0
    h = 0

    bot.send_message(message.from_user.id,"Хотите пройти тест\nещё раз - нажмите сюда => /go")


i = 0
bot.polling( none_stop = True, interval = 0 )


        
            






        
            



