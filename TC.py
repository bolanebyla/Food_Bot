class TC():

    def __init__(self, name=''):
        self.name = name
        self.FC = []

    def set_FC(self, list_FC=[]):
        self.FC = self.FC + list_FC




MK = TC('Модный квартал')

Noviy = TC('Новый')

#Galaktika = TC('Галактика')
#Galaktika.set_FC(['2 этаж','3 этаж'])

TC_list = [MK,Noviy]
