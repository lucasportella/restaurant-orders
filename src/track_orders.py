class TrackOrders:
    def __init__(self):
        self.orders = []
        self.costumers = set()
        self.meals = set()
        self.days = set()
        self.costumer_orders = {}

    def __len__(self):
        # O(1)
        return len(self.orders)

    def data_parser(self, costumer, meal, day):
        # O(1)
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
        # O(n)
        costumer_meals_counter = {}
        biggest = 0
        favorite = ""
        for meal, _day in self.costumer_orders[costumer]:
            if meal not in costumer_meals_counter:
                costumer_meals_counter[meal] = 1
            else:
                costumer_meals_counter[meal] += 1
            if costumer_meals_counter[meal] > biggest:
                biggest = costumer_meals_counter[meal]
                favorite = meal
        return favorite

    def get_never_ordered_per_costumer(self, costumer):
        # O(n)
        costumer_meals = set()
        for meal, _day in self.costumer_orders[costumer]:
            if meal not in costumer_meals:
                costumer_meals.add(meal)
        return self.meals.difference(costumer_meals)

    def get_days_never_visited_per_costumer(self, costumer):
        # O(n)
        costumer_days = set()
        for _meal, day in self.costumer_orders[costumer]:
            if day not in costumer_days:
                costumer_days.add(day)
        return self.days.difference(costumer_days)

    def get_busiest_day(self):
        days_counter = {}
        biggest = 0
        busiest = ""
        for _costumer, _meal, day in self.orders:
            if day not in days_counter:
                days_counter[day] = 1
            else:
                days_counter[day] += 1
            if days_counter[day] > biggest:
                biggest = days_counter[day]
                busiest = day
        return busiest

    def get_least_busy_day(self):
        # O(n+n)
        days_counter = {}
        for _costumer, _meal, day in self.orders:
            if day not in days_counter:
                days_counter[day] = 1
            else:
                days_counter[day] += 1

        smallest = False
        least_busy = ""
        for day, count in days_counter.items():
            if not smallest or count < smallest:
                smallest = count
                least_busy = day
        return least_busy
