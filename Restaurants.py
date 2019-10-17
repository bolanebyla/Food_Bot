class Restaurants():


    def __init__(self, id_rest, name='', tags=[]):
        self.id_rest = id_rest
        self.name = name
        self.tags=tags

    def set_address(self, TC='', haveFC=False or True, FС=''):
        self.TC = TC
        self.haveFC = haveFC
        if self.haveFC==True: 
            self.FС = FС

    def make_menu(selfe, menu):
        selfe.menu=menu




KFC = Restaurants('111111111','KFC', ['курица', 'напитки','бургеры'])
KFC.set_address('Модный квартал', False)

Shavuha_Petr2 = Restaurants('555555555','Шавуха от петрухи', ['шаурма', 'шаверма','шавуха'])
Shavuha_Petr2.set_address('Модный квартал', False)


MC_Duck = Restaurants('222222222','MC Duck', ['напитки','бургеры'])
MC_Duck.set_address('Комсомол', True, '2 этаж')

Shavuha_Petr1 = Restaurants('333333333','Шавуха от петрухи', ['шаурма', 'шаверма','шавуха'])
Shavuha_Petr1.set_address('Комсомол', True, '3 этаж')

No_eat = Restaurants('444444444','Лучше не ешь', ['кирпичи'])
No_eat.set_address('Новый', True, '3 этаж')
        
res_list = [KFC, MC_Duck, Shavuha_Petr1, No_eat, Shavuha_Petr2]


