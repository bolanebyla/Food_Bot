class Basket ():


    def __init__(self, id_rest, id_user):
        self.id_rest = id_rest
        self.id_user = id_user
        self.maked_basket = False
        self.basket = []
        

    def add_to_basket(self, thing=[]):
        self.basket = self.basket + thing
        self.maked_basket = True 


    def get_basket(self):
        return self.basket


