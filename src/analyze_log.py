import csv


def fav_meal(orders):
    meals = {}
    biggest = 0
    fav_meal = ''
    for order in orders:
        # order[0] must be the meal
        if order[0] not in meals:
            meals[order[0]] = 1
        else:
            meals[order[0]] += 1
        if meals[order[0]] > biggest:
            biggest = meals[order[0]]
            fav_meal = order[0]
    return fav_meal

def meal_counter(orders, meal):
    counter = 0
    for order in orders:
        if order[0] == meal:
            counter +=1
    return counter


def get_all_meals(path_to_file):
    meals = set()
    with open (path_to_file) as file:
        reader = csv.reader(file, delimiter=",", quotechar='"')
        for row in reader:
            if row[1] not in meals:
                meals.add(row[1])
    return meals

def client_meals(orders):
    meals = set()
    for order in orders:
        if order[0] not in meals:
            meals.add(order[0])
    return meals



def analyze_log(path_to_file):
    orders = {}
    with open (path_to_file) as file:
        reader = csv.reader(file, delimiter=",", quotechar='"')
        for row in reader:
            if row[0] not in orders:
                orders[row[0]] = [[row[1], row[2]]]
            else:
                orders[row[0]].append([row[1], row[2]])

    maria_fav_meal = fav_meal(orders['maria'])
    arnaldo_burguer_counter = meal_counter(orders['arnaldo'],'hamburguer')
    
    all_meals = get_all_meals('data/orders_1.csv')
    joao_meals = client_meals(orders['joao'])
    not_joao_meals = all_meals.difference(joao_meals)
    
       

analyze_log('data/orders_1.csv')






# dict of lists:
#  for row in reader:
#             if row[0] not in orders:
#                 orders[row[0]] = [row]
#             else:
#                 orders[row[0]].append(row)
#         print(orders)