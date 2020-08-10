import threading
import time
import copy
import cafeteria as cf


def fixed_input():
    """ This function will create a cafeteria object and give the hardcoded values to the attributes

    parametes : None

    returns : Cafeteria object

    """
    number_of_restaurants = 4
    number_of_items = 4
    list_of_dict_price = [{"A":3, "B":5, "C": 6, "D":7},{"A":7, "B":4, "E": 7, "F":6},{"A":5, "B":3, "E": 4, "C":7},{"E":3, "B":2, "C": 6, "F":7}]
    #list_of_dict_count = [{"A": 2, "B": 2, "C": 2}, {"A": 2, "B": 2, "C": 2}, {"A": 2, "B": 2, "C": 2}]
    processing_power = [5,5,5,5]

    cafeteria = cf.Cafeteria()
    cafeteria.set_restaurants_and_item_numbers(number_of_restaurants, number_of_items)
    cafeteria.set_prices(copy.deepcopy(list_of_dict_price))
    cafeteria.set_processing_power(processing_power)
    cafeteria.items_menu = ["A", "B", "C", "D", "E", "F"]

    return cafeteria

def custom_input():
    """ This function will create a cafeteria object and set the values of all attributes

    parametes : None

    returns : Cafeteria object

    """
    cafeteria = cf.Cafeteria()
    cafeteria.set_restaurants_and_item_numbers()
    cafeteria.set_prices()
    cafeteria.set_processing_power()
    print(cafeteria.number_of_restaurants)
    print(cafeteria.number_of_items)
    print(cafeteria.list_of_dict_price)
    print(cafeteria.processing_power)

    return cafeteria


def make_order(k, restaurant_index, cafeteria):
    """
    This function is going to be used to make a thread object
    :param k: total number of items
    :param restaurant_index: selected restaurant index for the order
    :param cafeteria: cafeteria object
    :return: None
    """
    cafeteria.processing_power[restaurant_index] -= k

    #waiting for the order to complete ( assuming 15 sec)
    time.sleep(15)

    cafeteria.processing_power[restaurant_index] += k

def take_order():
    """
    this function will take the std input from user for order.
    :return: order : dict of order (dish , quantity pair)
            k: total qunatity
    """
    order = dict()
    k = 0
    while True:
        dish_name, dish_number = input("enter the dish name and quantitiy seperated by space").split()
        dish_number = int(dish_number)
        order[dish_name] = dish_number
        k += dish_number
        q = input("for ending the order press 0 otherwise 1")
        if q == "0":
            break
    return order, k




if __name__ == "__main__":

    # we are taking the fixed_input , to take every input manually change it to custom_input()
    choice = int(input("enter 1 for the fixed input and enter 0 for the customize input"))
    if choice == 1:
        cafeteria = fixed_input()
    else:
        cafeteria = custom_input()

    while True:

        print()
        print("you can choose an item from = ",cafeteria.items_menu)
        print("please give your order")
        #taking order
        order, k = take_order()

        #choosing the right restaurant
        restaurant_index, order_price = cafeteria.choose_restaurant(order, k)
        if restaurant_index == -1:
            print("this order can not be completed please try to order one more time with different values")
            continue

        print("Restaurant",restaurant_index + 1,"is going to make this order and you need to pay",order_price," for this")

        #making the order
        thread = threading.Thread(target=make_order, args=(k, restaurant_index, cafeteria,))
        thread.start()







