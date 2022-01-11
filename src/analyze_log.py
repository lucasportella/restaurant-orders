import csv


def maria_fav_meal(orders):
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



def analyze_log(path_to_file):
    orders = {}
    with open (path_to_file) as file:
        reader = csv.reader(file, delimiter=",", quotechar='"')
        for row in reader:
            if row[0] not in orders:
                orders[row[0]] = [[row[1], row[2]]]
            else:
                orders[row[0]].append([row[1], row[2]])
    # only maria orders
    row1 = maria_fav_meal(orders['maria'])
    print(row1)
       

analyze_log('data/orders_1.csv')






# dict of lists:
#  for row in reader:
#             if row[0] not in orders:
#                 orders[row[0]] = [row]
#             else:
#                 orders[row[0]].append(row)
#         print(orders)