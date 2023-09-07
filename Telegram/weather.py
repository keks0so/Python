import pyowm
from colorama import init
from colorama import Fore, Back, Style
init()

print(Fore.BLACK)
print(Back.WHITE)


owm = pyowm.OWM('d86576be0c0e7501a1845bff77f26d8c')

place = input('А на этот раз откуда тебе погода нужна?: ')

mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
weather = observation.weather
weather.status           
weather.detailed_status


temp = temp_dict_celsius = weather.temperature('celsius')
wind = wind_dict_in_meters_per_sec = observation.weather.wind()   
wind_dict_in_meters_per_sec['speed']


print('Kороче в ' + place + 'е сейчас ' + w.get_detailed_status())
print('Температура где-то: ' + str(temp) + ' С')
print('А Скорость ветра ' + str(wind) + ' М/С')

if temp <= 10:
	print('Слушай, сейчас там реально холодно! \nдаже не думай подворачивать джинсы')
elif temp <=0:
    print('У тебя там чо зима что ли!? \nбез подштаников даже окно можешь не открывать')
elif temp <= -20: 
    print('Ну слушай, если ты оденешь 5 свитеров, \nто может быть у тебя есть шанс выжыть')
elif temp > 10:
	print('Будет достаточно лёгкой куртки')    
elif temp > 15:
	print('Ну чо погода норм, но куртку лучше возьми') 
elif temp >= 20:
	print('хватит майки (если стоять на солнышке)')
elif temp >= 23: 
	print('Погода кайф одевай что хочешь')
elif temp >= 27: 
	print('На улице жарко, но сгонять на речку самое то')
elif temp >= 32:
	print('Ты что решил загуглить температуру на солнце!? \nМой тебе совет включи кондицеонер')
if wind >= 9:
	print('Ах да и ещё: не забудь надеть ветровку, а главное - не бери зонт, \nа то улетишь вслед за Мери Попинс')
	