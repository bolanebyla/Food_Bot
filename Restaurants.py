class Restaurants():


    def __init__(self, id_rest, name=''):
        self.id_rest = id_rest
        self.name = name

    def set_address(self, TC='', haveFC = False , FС=''):
        self.TC = TC
        self.haveFC = haveFC
        if self.haveFC==True: 
            self.FС = FС

    def make_menu(selfe, menu):
        selfe.menu=menu




#Burger Heroes
Burger_Heroes1 = Restaurants('111111111','Burger Heroes')
Burger_Heroes1.set_address('Модный квартал')

Burger_Heroes2 = Restaurants('222222222','Burger Heroes')
Burger_Heroes2.set_address('Новый')

Burger_Heroes3 = Restaurants('333333333','Burger Heroes')
Burger_Heroes3.set_address('Галактика', True, '2 этаж')

#Шаверцыпа
ShaverCipa1 = Restaurants('444444444','Burger Heroes')
ShaverCipa1.set_address('Модный квартал')

ShaverCipa2 = Restaurants('555555555','Burger Heroes')
ShaverCipa2.set_address('Новый')

ShaverCipa3 = Restaurants('666666666','Burger Heroes')
ShaverCipa3.set_address('Галактика', True, '3 этаж')

#Food_Imperian

Food_Imperian1 = Restaurants('777777777','Food Imperion')
Food_Imperian1.set_address('Модный квартал')

Food_Imperian2 = Restaurants('888888888','Food Imperion')
Food_Imperian2.set_address('Галактика', True, '2 этаж')


#Pizza_house

Pizza_house1 = Restaurants('999999999','Pizza house')
Pizza_house1.set_address('Новый')

Pizza_house2 = Restaurants('999999991','Pizza house')
Pizza_house2.set_address('Галактика',True,'3 этаж')

        
res_list = [Burger_Heroes1, Burger_Heroes2, Burger_Heroes3, 
            ShaverCipa1, ShaverCipa2, ShaverCipa3, 
            Food_Imperian1, Food_Imperian2, Pizza_house1, Pizza_house2]


