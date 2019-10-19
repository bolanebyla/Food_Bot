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




KFC = Restaurants('111111111','KFC')
KFC.set_address('Модный квартал')

Shavuha_Petr2 = Restaurants('555555555','Шавуха от петрухи')
Shavuha_Petr2.set_address('Модный квартал')


#MC_Duck = Restaurants('222222222','MC Duck')
#MC_Duck.set_address('Комсомол', True, '2 этаж')

Shavuha_Petr1 = Restaurants('333333333','Шавуха от петрухи')
Shavuha_Petr1.set_address('Новый')

#No_eat = Restaurants('444444444','Лучше не ешь')
#No_eat.set_address('Новый', True, '3 этаж')
        
res_list = [KFC, Shavuha_Petr1, Shavuha_Petr2]


