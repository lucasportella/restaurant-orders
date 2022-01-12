class TrackOrders:
    def __init__(self):
        self.orders = []
        self.costumers = set()
        self.meals = set()
        self.days = set()
        self.costumer_orders = {}

    def __len__(self):
        return len(self.orders)

    def data_parser(self, costumer, meal, day):
        if costumer not in self.costumers:
            self.costumers.add(costumer)
        if meal not in self.meals:
            self.meals.add(meal)
        if day not in self.days:
            self.days.add(day)

        if costumer not in self.costumer_orders:
            self.costumer_orders[costumer] = [(meal, day)]
        else:
            self.costumer_orders[costumer].append((meal, day))
        

    def add_new_order(self, costumer, meal, day):
        self.orders.append((costumer, meal, day))
        self.data_parser(costumer, meal, day)
    

    def get_most_ordered_dish_per_costumer(self, costumer):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass


csv_parsed = [
    ["maria", "pizza", "terça-feira"],
    ["maria", "hamburguer", "terça-feira"],
    ["joao", "hamburguer", "terça-feira"],
    ["maria", "coxinha", "segunda-feira"],
    ["arnaldo", "misto-quente", "terça-feira"],
    ["jose", "hamburguer", "sabado"],
    ["maria", "hamburguer", "terça-feira"],
    ["maria", "hamburguer", "terça-feira"],
    ["joao", "hamburguer", "terça-feira"],
]

track1 = TrackOrders()

for costumer, meal, day in csv_parsed:
    track1.add_new_order(costumer, meal, day)

print(track1.costumer_orders)