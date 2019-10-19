class Menu():
    def __init__(self, name_rest='', id_rest=''):
        self.name_rest = name_rest
        self.id_rest = id_rest
        self.menu = []


    def add_element(self, category='', name='', price='', photo='', comp=''):
        self.menu.append([category, name, price, photo, comp])
            



KFC = Menu('KFC','111111111')
KFC.category = ['Бургеры', 'Твистеры']
KFC.category2 = 'Бургеры,Твистеры,Шаурма'

KFC.add_element('Бургеры','Чизбургер', '69', 'KFC(Burger)_Cheeseburger.png', 'Сыр')
KFC.add_element('Бургеры', 'Шефбургер Де Люкс', '159', 'KFC(Burger)_Shefburger.png','мясо')
KFC.add_element('Бургеры', 'Шефбургер Де Люкс острый', '159', 'KFC(Burger)_Shefburger_spisy.png','мясо, перец')

KFC.add_element('Твистеры', 'Твистер оригинальный', '174', 'KFC(Twister)_Twister_original.png', 'курица')
KFC.add_element('Твистеры', 'БоксМастер оригинальный', '214', 'KFC(Twister)_Box_master_original.png', 'курица')

Shavuha_Petr2 = Menu('Шавуха от петрухи','555555555')
Shavuha_Petr2.category=['Шаурма','Напитки']
Shavuha_Petr2.category2='Шаурма,напитки'

Shavuha_Petr2.add_element('Шаурма', 'Шаурма средняя', '150', 'Shavuha_Petr2(Shaurma)_Shaurma_midle.jpg', 'курица')
Shavuha_Petr2.add_element('Напитки', 'Вода байкалия', '40', 'BH_drinks_water.png', 'вода')


Shavuha_Petr1 = Menu('Шавуха от петрухи','333333333')
Shavuha_Petr1.category=['Шаурма','Напитки']
Shavuha_Petr1.category2='Шаурма,напитки'

Shavuha_Petr1.add_element('Шаурма', 'Шаурма средняя', '150', 'Shavuha_Petr2(Shaurma)_Shaurma_midle.jpg', 'курица')
Shavuha_Petr1.add_element('Напитки', 'Вода байкалия', '40', 'BH_drinks_water.png', 'вода')


menu_list = [KFC, Shavuha_Petr2, Shavuha_Petr1]

