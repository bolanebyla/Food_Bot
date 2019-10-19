class Basket ():


    def __init__(self, id_rest, id_user, basket ):
        self.id_rest = id_rest
        self.id_user = id_user
        self.basket = basket

        

    def add_to_basket(self, thing=[]):
        if thing == []:
            self.basket = []
        if thing!=[]:
            self.basket = self.basket + thing
        self.basket = self.basket + thing
        self.maked_basket = True 


    def get_basket(self):
        return self.basket


