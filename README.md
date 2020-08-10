# System-for-cafeteria

## Problem statment = 
The Cafeteria consist of N number of restaurants and every restaurant have M number of
different items. Every item has a different price at every restaurant.
Each restaurant has a processing power P for an order of K items, and always K <=P

### Conditions:
1) Once the restaurant takes the order, processing power will be reduced by K (ordered items)
of that restaurant.
2) An order can be placed at one restaurant. (All items should be ordered from a restaurant
which has the sufficient processing power and all items should available in restaurant)
3) Place the order in a restaurant that has the lowest price of the order.
4) Processing power will be restored on the completion of an order.

## Solution =
Assumption = quanitity of every item in a restaurant are unlimited. (for converting the code to limited itmes we just need to
uncomment the written line and add some extra line of codes).

command to run = python3 main.py

working =
    input = we can choose two methods for input the default one is the fixed input and for other we need to give manually.

    workflow = when order arrives we check for the best choice of restaurant and if found then we create a thread and decrease the
    value of processiong power and assume that it will takes around 15 sec to complete and after completion it will increment the
    processing power.
    after creating the thread we are ready for the next order. we dont have to wait to take the next order.
    at one time we can serve unlimted oreder.

    sample input =
        1 =
            A 2
            1
            B 1
            0
            output  = Restaurant 1 is going to make this order and you need to pay 11  for this.

            giving the next order befor 15 sec
            A 2
            1
            B 1
            0
            output = Restaurant 3 is going to make this order and you need to pay 13  for this

        2 =

            A 2
            1
            B 1
            0
            output  = Restaurant 1 is going to make this order and you need to pay 11  for this.

            giving the next order after 15 sec(first order is finished and preprocessing power is restored)
            A 2
            1
            B 1
            0
            output = Restaurant 1 is going to make this order and you need to pay 11  for this.
