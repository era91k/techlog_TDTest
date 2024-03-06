class CartePizzeria:

    def __init__(self):
        self.pizzas = []
    
    def is_empty(self):
        if self.nb_pizzas == 0:
            return True
        return False
    
    def nb_pizzas(self):
        return len(self.pizzas) 

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)
    
    def remove_pizza(self, name):
        for pizza in self.pizzas:
            if pizza.name == name:
                self.pizzas.remove(pizza)
                break
        raise CartePizzeriaException("Pizza n'existe pas")

class CartePizzeriaException(Exception):
    def __init__(self, message):
        super().__init__(message)

        

