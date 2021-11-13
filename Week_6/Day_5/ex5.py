class MenuItem:
    cursor = ''
    connection = ''

    def __init__(self, item_name, price, connection):
        self.item_name = item_name
        self.price = price
        MenuItem.connection = connection
        MenuItem.cursor = connection.cursor()

    def __repr__(self):
        return f'{self.item_name} {self.price}'

    def save(self):
        MenuItem.cursor.execute(
            f'INSERT INTO menu_items (item_name ,price) VALUES (\'{self.item_name}\', \'{self.price}\')'
        )
        MenuItem.connection.commit()
        print(
            f'{self.item_name} with the price of {self.price} was added successfully.')

    def delete(self):
        MenuItem.cursor.execute(
            f'delete from menu_items where item_name = \'{self.item_name}\''
        )
        MenuItem.connection.commit()
        print(f'{self.item_name} was deleted')

    def update(self, item_name, price):
        MenuItem.cursor.execute(
            f'update menu_items set item_name = \'{item_name}\', price = \'{price}\' where item_name = \'{self.item_name}\''
        )
        MenuItem.connection.commit()
        print(f'updated to {item_name} {price} successfully')

    def all(connection):
        cursor = connection.cursor()
        cursor.execute(f'select * from menu_items')
        item = cursor.fetchall()
        objects = [MenuItem(x[1], x[2], connection) for x in item]
        for obj in objects:
            print(obj)
        return objects

    def get_by_name(item_name, connection):
        cursor = connection.cursor()
        cursor.execute(
            f'select * from menu_items where item_name = \'{item_name}\'')
        obj = cursor.fetchone()
        if obj is None:
            return None
        return MenuItem(obj[1], int(obj[2]), connection)
