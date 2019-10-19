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

    print(message.from_user)

    chat_id = str(message.chat.id)
    bot.send_message(message.chat.id,'Привет, я твой помощник при заказе еды! ' + 
                     'Ты проголодался и хочешь быстро перекусить? Тогда тебе сюда! '+
                     'Скорее жми на "Новый заказ"!', reply_markup=keyboard_main_menu())
    info(chat_id)

    
    #basket = open('basket_'+str(message.chat.id)+'.txt', 'w')
    cleaning_basket(chat_id)

    order_list = open('order_list_'+str(message.chat.id)+'.txt', 'w')
    order_list.write('t' + chat_id[:4]+'1000\n')

@bot.message_handler(commands=['help'])
def start_message(message:Message):
    info(message.chat.id)

def cleaning_basket(chat_id):
     basket = open('basket_'+str(chat_id)+'.txt', 'w')

def info(chat_id):
    bot.send_message(chat_id, 'Для твоего удобства создан поиск ресторанов и кафе по интересующей тебя категории блюд. ' +
                     'Просто введи категорию сюда , и я подберу тебе список ресторанов, где есть такие блюда!')


# Основное меню
def keyboard_main_menu():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    btn1 = types.KeyboardButton('Новый заказ')
    btn2 = types.KeyboardButton('Корзина')
    markup.add(btn1, btn2)
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


    # После кнопки оплатить
    #if message.data[:-3] == 'pay':


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

        for i in Menu.menu_list:
            if id_rest == i.id_rest:
                keyboard_menu_list(i, category, chat_id)


    # Нажатие кнопки Добавить в корзину 1 шт.
    if message.data[-3:] == 'add':
        id_rest_new = message.data[:9]

        basket = open('basket_' + str(chat_id)+'.txt', 'r')
        s = basket.readlines()
        if s ==[]:
            id_rest = id_rest_new
        else:
            id_rest = s[-1][:9]

        if id_rest_new != id_rest :
            basket = open('basket_' + str(chat_id)+'.txt', 'w')
            bot.send_message(chat_id, 'Корзина обновлена')

        food_name = ''
        food_prise = ''
        k = -9
        f = False
        for i in message.data[9:-3]:
            if i=='*':
                f=True

            if i!='*' and f == False :
                food_name = food_name+i
                
            elif i!='*' and f == True :
                food_prise = food_prise+i
            k+=1
        
        basket = open('basket_' + str(chat_id)+'.txt', 'r')

        s = basket.readlines()

        if s==[]:
            s=[food_name+' 0\n']
            sum = 0
        else:
            sum = int(s[-1][16:-1])
            s = s[:-1]
            
        l = len(food_name)
        
        f = True
        for i in range(len(s)):
            if s[i][:l] == food_name:
                f = False
                kol = int(s[i][l+1:-1])
                kol = kol + 1
                
                sum = sum +int(food_prise)
                s[i]=food_name+ ' ' +str(kol)+'\n'

                basket = open ('basket_'+str(chat_id)+'.txt', 'w')
                for i in range(len(s)):
                    basket.write(s[i])
                break 
        bot.send_message(chat_id, 'Добавлено в корзину:\n' + food_name + '1 шт.')

        if f:
            s=s+[food_name+' 1\n']
            basket = open ('basket_'+str(chat_id)+'.txt', 'w')
            for i in range(len(s)):
                basket.write(s[i])
            sum = sum +int(food_prise)

        basket.write(id_rest_new+'Итого: '+str(sum)+'\n')


    # Нажатие кнопки Удалить из корзину 1 шт.
    if message.data[-3:] == 'del':

        id_rest_new = message.data[:9]

        basket = open('basket_' + str(chat_id)+'.txt', 'r')
        s = basket.readlines()
        if s ==[]:
            id_rest = id_rest_new
        else:
            id_rest = s[-1][:9]

        if id_rest_new != id_rest :
            basket = open('basket_' + str(chat_id)+'.txt', 'w')
            bot.send_message(chat_id, 'Корзина обновлена')

        food_name = ''
        food_prise = ''
        k = -9
        f = False
        for i in message.data[9:-3]:
            if i=='*':
                f=True

            if i!='*' and f == False :
                food_name = food_name+i
                
            elif i!='*' and f == True :
                food_prise = food_prise+i
            k+=1
        
        basket = open('basket_' + str(chat_id)+'.txt', 'r')

        s = basket.readlines()

        if s==[]:
            s=[food_name+' 0\n']
            sum = 0
             
        else:
            sum = int(s[-1][16:-1])
            s = s[:-1]
            
        l = len(food_name)
        
        f = True
        w = False
        for i in range(len(s)):
            if s[i][:l] == food_name:
                f = False
                kol = int(s[i][l+1:-1])
                if kol>0:
                    kol = kol - 1
                    w = True
                    sum = sum - int(food_prise)
                s[i]=food_name+ ' ' +str(kol)+'\n'

                basket = open ('basket_'+str(chat_id)+'.txt', 'w')
                for i in range(len(s)):
                    basket.write(s[i])
                break 

        if kol!=0 or w:
            bot.send_message(chat_id, 'Удалено из корзины:\n' + food_name + '1 шт.')

        if f or kol == 0 and not w:
            bot.send_message(chat_id, 'Этого элемента ещё нет в корзине')

        basket.write(id_rest_new+'Итого: '+str(sum)+'\n')



    # Нажатие кнопки Оплатить (форимрование списка)
    if message.data[-3:] == 'pay':
        id_rest = message.data[:-3]
        s_out = ''
        basket = open('basket_' + str(chat_id)+'.txt', 'r')
        s = basket.readlines()

        if s !=[]:

            bot.send_message(chat_id, 'Ваш заказ оплачен\nОжидайте👌') # Должен быть блок обработки платежа

            s=s[:-1]

            s_out = id_rest + '\n' + str(chat_id)+ '\n'
            for i in range(len(s)):
                s_out = str(s_out + s[i][:-1]) + ' шт.*'

            order_list = open('order_list_' + str(chat_id)+'.txt', 'r+')
            last_order =  order_list.readlines()#-2
            last_order = last_order[-1][:-1]

            number = last_order[5:]
            new_number = int(number)+1
            new_order=last_order[:-4]+str(new_number)
            order_list.write(new_order + '\n')

            order = open(new_order + '.txt', 'w')
            order.write(s_out)

            
        else:
             bot.send_message(chat_id, 'Этот заказ уже оплачен🤔\n'+
                             'Нажмите Новый заказ, чтобы создать новы😜👇')


    #Нажатие кнопки Очистить корзину 
    if message.data=='clean_basket':
        cleaning_basket(chat_id)
        bot.send_message(chat_id,'Корзина очищена😌')


         #После оплаты
    if message.data[-3:]=='pay':

        basket = open('basket_' + str(chat_id)+'.txt', 'r')
        s = basket.readlines()
        if s !=[]:
            cleaning_basket(chat_id)
            keyboard = types.InlineKeyboardMarkup()
            agry = 'Принять'
            order=''
            id_order = new_order #message.data[:-3]
            file=open(id_order+'.txt','r')
            data=file.readlines() #data[0]- id_rest; data[1]=id_user,data[2]-order
            for i in data[2]:
                if i=='*':order=order+'\n'
                else: order=order+i
            keyboard.add(types.InlineKeyboardButton(text=agry, callback_data=id_order+'agreed'))
            bot.send_message('891209550', 'Заказ №'+id_order+'\n'+order, reply_markup=keyboard)#891209550
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
        keyboard.add(types.InlineKeyboardButton(text=done, callback_data = id_order + 'done'))
        bot.send_message('-343953923','Заказ №'+id_order+'\n'+order, reply_markup=keyboard) 
        bot.send_message(data[1],'Ваша заказ № '+id_order+' принят!\n' +
                        'Ожидайте сообщения о готовности😊🕐')

        
    # Когда заказ выполнен
    if message.data[-4:]=='done':
        id_order=message.data[:9]
        order=''
        file=open(id_order+'.txt','r')
        data=file.readlines()
        for i in data[2]:
           if i=='*':order=order+'\n'
           else: order=order+i
        bot.send_message(data[1],'Ваша заказ № '+id_order+' готов! Пройдите к стойке выдачи заказа\n'+
                         'Приятного аппетита☺️')
        file.close()


    
# Обработка сообщений
@bot.message_handler(content_types=['text'])
def txt(message:Message):
    b = True # флаг проверки 'понял ли бот'
    # Новый заказ
    if message.text == 'Новый заказ':
        b = False
        bot.send_message(message.chat.id, "Выберите торговый центр", reply_markup = keyboard_TC_list())

    # Корзина
    if message.text =='Корзина':
        b = False
        bas_out= ''
        basket = open('basket_' + str(message.chat.id)+'.txt', 'r')
        s = basket.readlines()

        if s !=[]:
            id_rest = s[-1][:9]
            for i in range(len(s)-1):
                bas_out = str(bas_out + s[i][:-1]) + ' шт.\n'
    
            s[-1]=s[-1][9:-1]+' руб'
            bas_out = bas_out + '\n' + s[-1]

            for i in Restaurants.res_list:
                if i.id_rest == id_rest: 
                    restauran_name = i.name
                    break

            keyboard = types.InlineKeyboardMarkup()
            bt1 = 'Оплатить'
            bt2 = 'Очитстить корзину'
            keyboard.add(types.InlineKeyboardButton(text=bt1, callback_data = id_rest+'pay'))
            keyboard.add(types.InlineKeyboardButton(text=bt2, callback_data='clean_basket'))

            bot.send_message(message.chat.id, 'Ваша корзина')
            bot.send_message(message.chat.id, restauran_name + '\n\n' + bas_out, reply_markup = keyboard)

        else:
            bot.send_message(message.chat.id, 'Корзина пуста\n'+
                             'Нажмите Новый заказ, чтобы добавить что-нибудь в корзину😉👇')

    # Поиск по словам
    s = ''
    f = False # Флаг "нахождения категории по введённому слову" 
    for i in Menu.menu_list:

        for k in i.category:
            if message.text.lower() == k.lower():
                f = True 
                b = False
                s = s + i.name_rest + ' находится в ТЦ:\n'
                for j in Restaurants.res_list:
                    if j.name == i.name_rest:
                        s = s + j.TC+'\n'

        #if message.text.lower() in i.category2.lower():
    if f:
        bot.send_message(message.chat.id, 'Список заведений где ты сможешь это найти:')
        bot.send_message(message.chat.id,s)
        bot.send_message(message.chat.id, 'Не благодари 😘')
    
    if b:
        bot.send_message(message.chat.id, 'Я тебя не понял😢')
        bot.send_message(message.chat.id, 'Лечше сделай новый заказ😊')


        



bot.polling()