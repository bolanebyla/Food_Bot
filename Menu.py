class Menu():
    def __init__(self, name_rest='', id_rest=''):
        self.name_rest = name_rest
        self.id_rest = id_rest
        self.menu = []


    def add_element(self, category='', name='', price='', photo='', comp=''):
        self.menu.append([category, name, price, photo, comp])
            




Burger_heroes1 = Menu('Burger heroes','111111111')
Burger_heroes1.category = ['Бургеры','Твистеры','Напитки']

Burger_heroes1.add_element('Бургеры','Классика', '180', 'BH_burgers_Classic.png', '')
Burger_heroes1.add_element('Бургеры', 'Царь-бургер', '580', 'BG_burgers_car_burger.png','')
Burger_heroes1.add_element('Бургеры', 'Light-Burg', '410', 'BG_burgers_ light.png','')
Burger_heroes1.add_element('Бургеры','Spicy-Burg', '220', 'BH_burgers_spicyburg.png', '')
Burger_heroes1.add_element('Твистеры', 'Цезролл', '190', 'BH_roll_cezroll.png','')
Burger_heroes1.add_element('Твистеры', 'Smallbeff', '210', 'BH_roll_smallbeef.png','')
Burger_heroes1.add_element('Напитки','Ягодное смузи', '195', 'BH_drinks_jagodnoe_smuzi.png', '')
Burger_heroes1.add_element('Напитки', 'Вода Baickalia', '40', 'BH_drinks_water.png','')
Burger_heroes1.add_element('Напитки', 'Моле-кола', '75', 'BH_drinks_molecola.png','')


Burger_heroes2 = Menu('Burger heroes','222222222')
Burger_heroes2.category = ['Бургеры','Твистеры','Напитки']

Burger_heroes2.add_element('Бургеры','Классика', '180', 'BH_burgers_Classic.png', '')
Burger_heroes2.add_element('Бургеры', 'Царь-бургер', '580', 'BG_burgers_car_burger.png','')
Burger_heroes2.add_element('Бургеры', 'Light-Burg', '410', 'BG_burgers_ light.png','')
Burger_heroes2.add_element('Бургеры','Spicy-Burg', '220', 'BH_burgers_spicyburg.png', '')
Burger_heroes2.add_element('Твистеры', 'Цезролл', '190', 'BH_roll_cezroll.png','')
Burger_heroes2.add_element('Твистеры', 'Smallbeff', '210', 'BH_roll_smallbeef.png','')
Burger_heroes2.add_element('Напитки','Ягодное смузи', '195', 'BH_drinks_jagodnoe_smuzi.png', '')
Burger_heroes2.add_element('Напитки', 'Вода Baickalia', '40', 'BH_drinks_water.png','')
Burger_heroes2.add_element('Напитки', 'Моле-кола', '75', 'BH_drinks_molecola.png','')


Burger_heroes3 = Menu('Burger heroes','333333333')
Burger_heroes3.category = ['Бургеры','Твистеры','Напитки']

Burger_heroes3.add_element('Бургеры','Классика', '180', 'BH_burgers_Classic.png', '')
Burger_heroes3.add_element('Бургеры', 'Царь-бургер', '580', 'BG_burgers_car_burger.png','')
Burger_heroes3.add_element('Бургеры', 'Light-Burg', '410', 'BG_burgers_ light.png','')
Burger_heroes3.add_element('Бургеры','Spicy-Burg', '220', 'BH_burgers_spicyburg.png', '')
Burger_heroes3.add_element('Твистеры', 'Цезролл', '190', 'BH_roll_cezroll.png','')
Burger_heroes3.add_element('Твистеры', 'Smallbeff', '210', 'BH_roll_smallbeef.png','')
Burger_heroes3.add_element('Напитки','Ягодное смузи', '195', 'BH_drinks_jagodnoe_smuzi.png', '')
Burger_heroes3.add_element('Напитки', 'Вода Baickalia', '40', 'BH_drinks_water.png','')
Burger_heroes3.add_element('Напитки', 'Моле-кола', '75', 'BH_drinks_molecola.png','')



ShaverCipa1 = Menu('Шаверцыпа',444444444)
ShaverCipa1.category = ['Шаурма','Шашлык','Напитки']

ShaverCipa1.add_element('Шаурма','Овощная', '140', 'cipa_chaurma_vegetables.png', '')
ShaverCipa1.add_element('Шаурма', 'Куриная', '180', 'cipa_chaurma_chicken.png','')
ShaverCipa1.add_element('Шашлык', 'Шашлык свиной', '380', 'cipa_chachlik_pork.png','')
ShaverCipa1.add_element('Шашлык','Шашлык куриный', '310', 'cipa_chachlik_chicken.png', '')
ShaverCipa1.add_element('Напитки', 'Чай авторский', '410', 'cipa_drinks_tea.png','')
ShaverCipa1.add_element('Напитки','Espresso', '120', 'cipa_drinks_espresso.png', '')
ShaverCipa1.add_element('Напитки', 'Апельсиновый фреш',' 180', 'cipa_drinks_orange_fresh.png','')



ShaverCipa2 = Menu('Шаверцыпа', 555555555)
ShaverCipa2.category = ['Шаурма','Шашлык','Напитки']

ShaverCipa2.add_element('Шаурма','Овощная', '140', 'cipa_chaurma_vegetables.png', '')
ShaverCipa2.add_element('Шаурма', 'Куриная', '180', 'cipa_chaurma_chicken.png','')
ShaverCipa2.add_element('Шашлык', 'Шашлык свиной', '380', 'cipa_chachlik_pork.png','')
ShaverCipa2.add_element('Шашлык','Шашлык куриный', '310', 'cipa_chachlik_chicken.png', '')
ShaverCipa2.add_element('Напитки', 'Чай авторский', '410', 'cipa_drinks_tea.png','')
ShaverCipa2.add_element('Напитки','Espresso', '120', 'cipa_drinks_espresso.png', '')
ShaverCipa2.add_element('Напитки', 'Апельсиновый фреш', '180', 'cipa_drinks_orange_fresh.png','')



ShaverCipa3 = Menu('Шаверцыпа', 666666666)
ShaverCipa3.category = ['Шаурма','Шашлык','Напитки']

ShaverCipa3.add_element('Шаурма','Овощная', '140', 'cipa_chaurma_vegetables.png', '')
ShaverCipa3.add_element('Шаурма', 'Куриная', '180', 'cipa_chaurma_chicken.png','')
ShaverCipa3.add_element('Шашлык', 'Шашлык свиной', '380', 'cipa_chachlik_pork.png','')
ShaverCipa3.add_element('Шашлык','Шашлык куриный', '310', 'cipa_chachlik_chicken.png', '')
ShaverCipa3.add_element('Напитки', 'Чай авторский', '410', 'cipa_drinks_tea.png','')
ShaverCipa3.add_element('Напитки','Espresso', '120', 'cipa_drinks_espresso.png', '')
ShaverCipa3.add_element('Напитки', 'Апельсиновый фреш', '180', 'cipa_drinks_orange_fresh.png','')


Food_Imperian1 = Menu('Food Imperian', 777777777)
Food_Imperian1.category = ['Пицца','Суши','Напитки']

Food_Imperian1.add_element('Пицца','Mia', '420', 'FI_pizza_Mia.png', '')
Food_Imperian1.add_element('Пицца','Dor.Pomidor', '390', 'FI_pizza_dor.pomidor.png', '')
Food_Imperian1.add_element('Суши','Элит', '335', 'FI_suchsi_elit.png', '')
Food_Imperian1.add_element('Суши','Simple', '120', 'FI_suchsi_simple.png', '')
Food_Imperian1.add_element('Суши','warmfish', '210', 'FI_suchsi_warmfish.png', '')
Food_Imperian1.add_element('Напитки','Молочный коктейль', '120', 'FI_drinks_milk_mix.png', '')
Food_Imperian1.add_element('Напитки','Зеленый чай', '70', 'FI_drinks_green_tea.png', '')


Food_Imperian2 = Menu('Food Imperian', 888888888)
Food_Imperian2.category = ['Пицца','Суши','Напитки']

Food_Imperian2.add_element('Пицца','Mia', '420', 'FI_pizza_Mia.png', '')
Food_Imperian2.add_element('Пицца','Dor.Pomidor', '390', 'FI_pizza_dor.pomidor.png', '')
Food_Imperian2.add_element('Суши','Элит', '335', 'FI_suchsi_elit.png', '')
Food_Imperian2.add_element('Суши','Simple', '120', 'FI_suchsi_simple.png', '')
Food_Imperian2.add_element('Суши','warmfish', '210', 'FI_suchsi_warmfish.png', '')
Food_Imperian2.add_element('Напитки','Молочный коктейль', '120', 'FI_drinks_milk_mix.png', '')
Food_Imperian2.add_element('Напитки','Зеленый чай', '70', 'FI_drinks_green_tea.png', '')



Pizza_house1 = Menu('Pizza house', 999999999)
Pizza_house1.category = ['Пицца','Напитки']
Pizza_house1.add_element('Пицца','Me.Saus', '350', 'PH_pizza_mr_saus.png', '')
Pizza_house1.add_element('Пицца','Old School', '295', 'PH_pizza_old_school.png', '')
Pizza_house1.add_element('Напитки','Горячий шоколад', '90', 'PH_drinks_hot_schocolate.png', '')
Pizza_house1.add_element('Напитки','Cappuchino', '135', 'PH_drinks_cappuchino.png', '')


Pizza_house2 = Menu('Pizza house', 999999991)
Pizza_house2.category = ['Пицца','Напитки']
Pizza_house2.add_element('Пицца','Me.Saus', '350', 'PH_pizza_mr_saus.png', '')
Pizza_house2.add_element('Пицца','Old School', '295', 'PH_pizza_old_school.png', '')
Pizza_house2.add_element('Напитки','Горячий шоколад', '90', 'PH_drinks_hot_schocolate.png', '')
Pizza_house2.add_element('Напитки','Cappuchino', '135', 'PH_drinks_cappuchino.png', '')


menu_list = [Burger_heroes1, Burger_heroes2, Burger_heroes3, 
            ShaverCipa1, ShaverCipa2, ShaverCipa3, 
            Food_Imperian1, Food_Imperian2, Pizza_house1, Pizza_house2]

