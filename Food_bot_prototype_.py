import telebot

import TC
import Restaurants
import Basket 
import Orders
import Menu


import config

from telebot import types
from telebot.types import Message



bot = telebot.TeleBot(config.TOKEN)




# /start
@bot.message_handler(commands=['start'])
def start_message(message:Message):
    last_buton = 'start'
    bot.send_message(message.chat.id,'Привет, я test2_bot!', reply_markup=keyboard_main_menu())
    print ('Start')

    #bot.send_photo(message.chat.id, open('KFC(Twister)_Box_master_original.png', 'rb'))

# /new
@bot.message_handler(commands=['new'])
def new(message:Message):
    global b1
    b1 = Basket.Basket(123, message.from_user.id)

# /add
@bot.message_handler(commands=['add'])
def add(message:Message):
   
    b1.add_to_basket(['курочка']) 
    print(b1.get_basket())

# Основное меню
def keyboard_main_menu():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    btn1 = types.KeyboardButton('Новый заказ')
    btn2 = types.KeyboardButton('Корзина')
    btn3 = types.KeyboardButton('Статус заказа')
    markup.add(btn1, btn2, btn3)
    return markup


# Меню Список ТЦ
def keyboard_TC_list():
	keyboard = types.InlineKeyboardMarkup()

	for i in TC.TC_list:
		keyboard.add(types.InlineKeyboardButton(text=i.name, callback_data=i.name + 'TC'))
        #keyboard.add(types.InlineKeyboardButton(text=i.name, callback_data=i.name))
	return keyboard


# Проверка наличия фудкорта
def check_FC(TC_in, chat_id):
    for i in TC.TC_list:
        if i.name == TC_in:
            if i.FC == []:
                bot.send_message(chat_id, i.name + '\n' + "Выберите кафе/ресторан", 
                                 reply_markup = keyboard_res_list(TC_in, ''))  
            else:
                bot.send_message(chat_id, i.name + '\n' + "Выберите фуд-корт", 
                                 reply_markup = keyboard_FC_list(i.name, i.FC))


# Меню фудкорты
def keyboard_FC_list(TC_name, FC_in):
    keyboard = types.InlineKeyboardMarkup()

    for i in FC_in:
        keyboard.add(types.InlineKeyboardButton(text = i, callback_data = TC_name+ ' ' + i+'FC'))

    return keyboard



# Меню Список рестаранов и кафе
def keyboard_res_list(TC_in, FC=''):
    keyboard = types.InlineKeyboardMarkup()

    if FC=='':
        for i in Restaurants.res_list:
            if i.TC == TC_in:
                keyboard.add(types.InlineKeyboardButton(text = i.name, callback_data = i.id_rest + 'kat'))

    else:
        for i in Restaurants.res_list:
            if i.TC == TC_in and i.FС == FC:
                keyboard.add(types.InlineKeyboardButton(text = i.name, callback_data = i.id_rest + 'kat'))

    return keyboard

 # Меню Список категорий ресторана
def keyboard_category_list(m, chat_id):
    keyboard = types.InlineKeyboardMarkup()
    for i in m.category:
         keyboard.add(types.InlineKeyboardButton(text = i, callback_data = m.id_rest + i + 'name_f'))
    bot.send_message(chat_id, m.name_rest + '\n' + "Выберите категорию", 
                                 reply_markup = keyboard)

# Меню Список товаров из категории
def keyboard_menu_list(c, category, chat_id):
    keyboard = types.InlineKeyboardMarkup()
    bot.send_message(chat_id, 'Категория '+category)
    id_rest = c.id_rest
    for i in range(len(c.menu)):#-1
        if c.menu[i][0] == category:
            food_name = c.menu[i][1]
            food_prise = c.menu[i][2]

            keyboard = types.InlineKeyboardMarkup()
            bot.send_photo(chat_id, open(c.menu[i][3], 'rb'))
            add_to_Basket = 'Добавить в корзину 1 шт. '+ c.menu[i][1]
            keyboard.add(types.InlineKeyboardButton(text = add_to_Basket, callback_data =id_rest+food_name+
                                                    '*'+food_prise+'add'))
                                                  
            delete = 'Убрать из корзины 1 шт. '+ c.menu[i][1]
            keyboard.add(types.InlineKeyboardButton(text = delete, callback_data =id_rest+food_name+
                                                    '*'+food_prise+'del'))
            bot.send_message(chat_id, 'Состав: '+ c.menu[i][4], reply_markup = keyboard)
            keyboard = []


# Обработка ответов от чат-клавиатуры
@bot.callback_query_handler(func=lambda message:True)
def ans(message:Message):
    chat_id = message.message.chat.id

    # После выбора ТЦ
    # Проверяем есть ли у выбранного ТЦ фудкорты
    if message.data[-2:] =='TC':
        for i in TC.TC_list:
            if message.data[:-2] == i.name:
                check_FC(i.name, chat_id)

    # После выбора фуд-корта
    if message.data[-2:] == 'FC':
        for i in TC.TC_list:
            for j in range(len(i.FC)):
                if message.data == i.name+' '+i.FC[j]+'FC':
                    bot.send_message(chat_id, i.name + ' (' + i.FC[j] +')' + '\n' + "Выберите кафе/ресторан", 
                                     reply_markup = keyboard_res_list(i.name, i.FC[j]))

    #после выбора ресторана
    if message.data[-3:] == 'kat':
        id_rest = message.data[:-3]
        
        for i in Menu.menu_list:
            if id_rest == i.id_rest:
                keyboard_category_list(i, chat_id)


    # После выбора списка категорий
    if message.data[-6:] == 'name_f':
        id_rest = message.data[:9]
        category = message.data[9:-6]
        print(category)
        for i in Menu.menu_list:
            if id_rest == i.id_rest:
                keyboard_menu_list(i, category, chat_id)


    # Нажатие кнопки Добавить в корзину 1 шт.
    if message.data[-3:] == 'add':
        id_rest = message.data[:-9]

        food_name = ''
        k = -9
        for i in message.data[9:-3]:
            if i == '*':
                break
            if i!='*':
                food_name = food_name+i
                print(i)
                k+=1
        print(food_name)



            

    # Нажатие кнопки Удалить из корзину 1 шт.
    print(message.data)
    print(message.data[9:-3])

                








# Обработка сообщений
@bot.message_handler(content_types=['text'])
def txt(message:Message):
    if message.text == 'Новый заказ':
        bot.send_message(message.chat.id, "Выберите торговый центр", reply_markup = keyboard_TC_list())
        


bot.polling()



