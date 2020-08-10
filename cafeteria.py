class Cafeteria:

    def __init__(self):
        self.number_of_restaurants = 3
        self.number_of_items = 3
        self.list_of_dict_price = [dict()]
        #self.list_of_dict_count = M_count
        self.processing_power = [5,5,5]
        self.items_menu = []

    def set_restaurants_and_item_numbers(self, N = -1, M = -1):
        if N != -1 and M != -1:
            self.number_of_restaurants = N
            self.number_of_items = M
            return
        self.number_of_restaurants = int(input("Enter the number of restaurants"))
        self.number_of_items = int(input("Enter the number of items"))


    def set_prices(self, list_of_dict_price = None):
        """
        if calling without parameter then it will ask to enter the price of all the items in the resturant
        and if price is passed then it will set the price accordingly.
        :param list_of_dict_price: list of dict of price of every item according to every restaurant
        :return: None
        """
        if list_of_dict_price != None:
            self.list_of_dict_price = list_of_dict_price
            return

        self.list_of_dict_price = []
        self.items_menu = []
        for i in range(self.number_of_restaurants):
            print("enter the dish name and price for the restaurant", i + 1)
            temp = dict()
            for j in range(self.number_of_items):
                item_name, item_price = input("Enter the dish name and price seperated by space").split()
                item_price = int(item_price)
                temp[item_name] = item_price

                if item_name not in self.items_menu:
                    self.items_menu.append(item_name)

            self.list_of_dict_price.append(temp)

    def set_processing_power(self, p_p = None):
        """
        If calling without parameter then it will ask to enter processing power otherwise set the processing power to given
        values.
        :param p_p: list of processing power
        :return: None
        """
        if p_p != None:
            self.processing_power = p_p
            return

        self.processing_power = []
        for i in range(self.number_of_restaurants):
            self.processing_power.append(int(input("enter the processing power of restaurant" +  str(i + 1))))



    def choose_restaurant(self, order, k):
        """
        It will take the order which is dict of item and quantity pair ,and the total qunatity.
        then it will check for the two condition = (All items should be ordered from a restaurant
        which has the sufficient processing power and all items should available in restaurant). If no restaurant
        can take the order the function will return -1 as index.

        :param order: order dict which is dict of item and quantity pair
        :param k: total qunatity of the order
        :return: choose restaurant index and total price of that order.
        """

        #finding the index of desired restaurant
        restaurant_index = -1
        min_price = 0
        for i in range(self.number_of_restaurants):
            if k > self.processing_power[i]:
                continue

            temp_price = 0
            flag = 0

            for j in order:
                #if self.list_of_dict_count[j] < order[j]:
                    #flag = 1
                    #break
                if self.list_of_dict_price[i].get(j) == None:
                    flag = 1
                    break

                temp_price += self.list_of_dict_price[i][j]*order[j]

            if flag == 0:
                if restaurant_index != -1:
                    if temp_price < min_price:
                        min_price = temp_price
                        restaurant_index = i
                else:
                    min_price = temp_price
                    restaurant_index = i

        return restaurant_index, min_price