class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.ingredients = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
        self.inventory = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }
        self.quantities_to_buy = {
        'pao': 0,
        'carne': 0,
        'queijo': 0,
        'molho': 0,
        'presunto': 0,
        'massa': 0,
        'frango': 0,
    }

    def add_new_order(self, costumer, meal, day):
        for ingredient in self.ingredients[meal]:
            if self.inventory[ingredient] == 0:
                return False
        for ingredient in self.ingredients[meal]:
            self.quantities_to_buy[ingredient] += 1
            


    def get_quantities_to_buy(self):
        return self.quantities_to_buy

    def get_available_dishes(self):
        pass