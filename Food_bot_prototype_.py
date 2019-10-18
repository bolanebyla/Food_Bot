import telebot

import TC
import Restaurants
import Basket 
import Orders
import Menu


import config

from telebot import types
from telebot.types import Message

#925219221 pc

bot = telebot.TeleBot(config.TOKEN)




# /start
@bot.message_handler(commands=['start'])
def start_message(message:Message):
    print('BotActivated')
    last_buton = 'start'
    bot.send_message(message.chat.id,'Привет, я test2_bot!', reply_markup=keyboard_main_menu())
    keyboard = types.InlineKeyboardMarkup()
    pay = 'Оплатить'
    keyboard.add(types.InlineKeyboardButton(text=pay, callback_data='111222333pay'))
    bot.send_message(message.chat.id,'Оплатите заказ', reply_markup=keyboard)

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
    bot.send_message(chat_id, category)
    for i in range(len(c.menu)):#-1
        if c.menu[i][0] == category:
            keyboard = types.InlineKeyboardMarkup()
            bot.send_photo(chat_id, open(c.menu[i][3], 'rb'))
            out = 'Добавить в корзину '+ c.menu[i][1]
            keyboard.add(types.InlineKeyboardButton(text = out,callback_data ='0'))# callback_data = с.id_rest + 
                                                   # c.menu[i][2] + 'что-то'))
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
                
    #После оплаты
    if message.data[-3:]=='pay':
        keyboard = types.InlineKeyboardMarkupь()
        agry = 'Принять'
        order=''
        id_order=message.data[:-3]
        file=open(id_order+'.txt','r')
        data=file.readlines() #data[0]- id_rest; data[1]=id_user,data[2]-order
        for i in data[2]:
            if i=='*':order=order+'\n'
            else: order=order+i
        keyboard.add(types.InlineKeyboardButton(text=agry, callback_data=id_order+'agreed'))
        bot.send_message('891209550','Заказ №'+id_order+'\n'+order, reply_markup=keyboard)
        file.close()
    
    #После подтвержения принятия заказа
    if message.data[-6:]=='agreed':
        done='Выполнен'
        order=''
        keyboard = types.InlineKeyboardMarkup()
        id_order=message.data[:-6]
        file=open(id_order+'.txt','r')
        data=file.readlines()
        for i in data[2]:
           if i=='*':order=order+'\n'
           else: order=order+i
        keyboard.add(types.InlineKeyboardButton(text=done,callback_data=id_order+'done'))
        bot.send_message('925219221','Заказ №'+id_order+'\n'+order,reply_markup=keyboard)
        bot.send_message(data[1],'Ваша заказ № '+id_order+' принят! Ожидайте сообщения о готовности:)')
        file.close()
    
    if message.data[-4:]=='done':
        id_order=message.data[:9]
        order=''
        file=open(id_order+'.txt','r')
        data=file.readlines()
        for i in data[2]:
           if i=='*':order=order+'\n'
           else: order=order+i
        bot.send_message(data[1],'Ваша заказ № '+id_order+' готов! Пройдите к стойке приема)')
        file.close()
    





# Обработка сообщений
@bot.message_handler(content_types=['text'])
def txt(message:Message):
    if message.text == 'Новый заказ':
        bot.send_message(message.chat.id, "Выберите торговый центр", reply_markup = keyboard_TC_list())
    keyboard = types.InlineKeyboardMarkup() 
    if message.text.lower() in str(Menu.category_list).lower():
        for i in Menu.menu_list:
            if message.text.lower() == str(i.menu[0][0]).lower():
                keyboard.add(types.InlineKeyboardButton(text=i.name_rest,callback_data=i.id_rest+'kat'))
        bot.send_message(message.chat.id,'Вот туть есть то, что ты искал:', reply_markup=keyboard)


bot.polling()



