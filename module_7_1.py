class Product ():

    def __init__(self, name, weight: float, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop():

    def __init__(self):
        self.__file_name =  'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        print(file.read())
        file.close()

    def add(self, *products):
        file = open(self.__file_name, 'r+')
        lines = file.readlines()
        for product in products:
            is_product = False
            for line in lines:
                if product.name in line:
                    #file.write('\n' + f'Продукт {product.name} уже есть в магазине')
                    file.write(str('\n Продукт уже есть в магазине'))
                    is_product = True
                    break
            if is_product == False:
                file.write('\n' + str(product))
        file.close()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
p4 = Product('Apple', 3, 'Fruit')

print(p2)

s1 = Shop()
s1.add(p1, p2, p3, p4)

print(s1.get_products())