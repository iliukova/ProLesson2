# Ресторан надає можливість зробити онлайн замовлення страв.
# Розмір знижки по замовленню залежить від карти лояльності, яку має клієнт: Regular, Silver або Gold.
# Необхідно написати Python-скрипт, який буде повертати вартість зробленого замовлення.
# Для реалізації різних типів карток лояльності необхідно використовувати наслідування.

class Discount:
    def __init__(self, rate: float = 0):
        self.__rate = rate

    def discount(self):
        return self.__rate


class RegularDiscount(Discount):
    def __init__(self, rate=0.1):
        super().__init__(rate)


class SilverDiscount(Discount):
    def __init__(self, rate=0.2):
        super().__init__(rate)


class GoldDiscount(Discount):
    def __init__(self, rate=0.3):
        super().__init__(rate)


class Product:

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}: {self.price:.2f}'


class Cart:

    def __init__(self):
        self.products = []
        self.quantities = []

    def add_product(self, product, quantity=1):
        self.products.append(product)
        self.quantities.append(quantity)

    def total(self):
        return sum(product.price * quantity for product, quantity in zip(self.products, self.quantities))

    def __str__(self):
        res = ''
        for product, quantity in zip(self.products, self.quantities):
            res += f'{product} x {quantity} = {product.price * quantity} грн\n'
        return res


class Client:
    def __init__(self, name: str, discount: Discount):
        self.name = name
        self.discount = discount

    def get_total_price(self, order: Cart):
        return order.total() * (1 - self.discount.discount())


cart = Cart()
pr_1 = Product('banana', 10)
pr_2 = Product('apple', 20)
pr_3 = Product('orange', 30)

cart.add_product(pr_1)
cart.add_product(pr_2, 3)
cart.add_product(pr_3, 2)

client = Client('User 1', RegularDiscount())
print(client.get_total_price(cart))