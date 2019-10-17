class TC():

    def __init__(self, name=''):
        self.name = name
        self.FC = []

    def set_FC(self, list_FC=[]):
        self.FC = self.FC + list_FC




MK = TC('Модный квартал')

Komsomol = TC('Комсомол')
Komsomol.set_FC(['2 этаж','3 этаж'])

Novi = TC('Новый')
Novi.set_FC(['2 этаж','3 этаж'])

TC_list = [MK,Komsomol,Novi]
