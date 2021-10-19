menu = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
"""
print(menu)
listMenu = [
    "wings", "cookies", "spring rolls", "salmon", "steak", "meat tornado",
    "a literal garden", "ice cream", "cake", "pie", "coffee", "tea",
    "unicorn Tears"
]

def orders():
    order = []
    selection = input('> ').lower()
    while selection.lower() != 'quit':
        if selection.lower() in listMenu:
            order.append(selection)
            print(f"* {order.count(selection)} order of {selection} have been added to your meal *")
        else:
            print('make a selection from the menu!')
        selection = input('> ')
if __name__ == '__main__':
    orders()
