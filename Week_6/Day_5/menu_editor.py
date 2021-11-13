from ex5 import MenuItem
import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'letmein'
DATABASE = 'Restaurant'


connection = psycopg2.connect(
    host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE
)


def show_user_menu():
    # displays the program menu
    while True:
        i = input('''
        MENU
        (a) Add an item
        (d) Delete an item
        (u) Update an item
        (v) View the menu
        (x) Exit
        ''')

        # add
        if i == 'a':
            while True:
                item = input('Enter item:\n')
                price = input(f'Enter price for {item}:\n')
                while not price.isnumeric:
                    price = input('Invalid price\n')
                return add_item_to_menu(item, price)

        # delete
        elif i == 'd':
            while True:
                item = input('Enter item:\n')
                return remove_item_from_menu(item)

        # update
        elif i == 'u':
            while True:
                i = input('Enter item:\n')
                item = MenuItem.get_by_name(i, connection)
                if item == None:
                    print(f'Sorry, {i} not found')
                    return show_user_menu()
                return update_item(item)

        # view menu
        elif i == 'v':
            show_restaurant_menu()

        # exit
        elif i == 'x':
            break
        else:
            print('invalid input')


def add_item_to_menu(item, price):
    item = MenuItem(item, price, connection)
    item.save()
    return show_user_menu()


def remove_item_from_menu(item):
    item = MenuItem.get_by_name(item, connection)
    if (item == None):
        print('Somthing went wrong, no such item found\n')
    else:
        item.delete()
    return show_user_menu()


def update_item(item):
    while True:
        item = input(
            'Enter the new name or leave empty for default:\n')
        if item == '':
            item = item.item

        price = input(
            f'Enter new price for {item} or leave empty for default:\n')
        if price == '':
            price = item.price
        else:
            while not price.isnumeric:
                price = input('Invalid price, please try again:\n')
        item.update(item, price)
        return show_user_menu()


def show_restaurant_menu():
    MenuItem.all(connection)


show_user_menu()
connection.close()
