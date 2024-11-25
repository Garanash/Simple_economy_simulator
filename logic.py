import random

FORM = ['romb', 'triangle', 'circle', 'star', 'halfmoon']  # 'Star', 'Half-moon'
COLOR = ['#b22222', '#0a7e07', '#3e37ff', '#fded00', '#b24bf3']  # 'Yellow', 'Purple'
PRICE_COLOR = {'#b22222': 1.5, '#0a7e07': 1.7, '#3e37ff': 1.9, '#fded00': 2.1, '#b24bf3': 2.3}
PRICE_FORM = {"romb": 10, 'triangle': 20, "circle": 30, 'star': 40, 'halfmoon': 50}


class Seller:
    def __init__(self, name, money: int) -> None:
        self.name = name
        self.START_MONEY = money  # для статистики
        self.money = money
        self.tool = 0
        self.reserve = []
        self.products = []

    def statistic_move(self):
        return self.money - self.START_MONEY

    def buy_tool(self):
        if not self.tool and self.money >= 50:
            self.tool = 5
            self.money -= 50
        else:
            return 0

    def produce(self, elem):
        price = {'#3e37ff': 10, '#0a7e07': 20, '#b22222': 30, '#fded00': 40, '#b24bf3': 50}
        if self.tool and self.money >= price[elem.color]:
            self.tool -= 1
            self.money -= price[elem.color]
            self.products.append(Item(elem.color, elem.form, self))
        else:
            pass

    def send_product_on_market(self, market):
        if self.products:
            market.showcase.extend(self.products)
            self.products = []
        else:
            return 0

    def __repr__(self):
        return f'{self.name} {self.money}'

    def strategy(self):
        def alg1():
            if not self.tool:
                self.buy_tool()
            else:
                while self.money // 10 > 0:
                    self.tool -= 1
                    self.money -= 10
                    self.products.append(Item('#3e37ff', 'romb', self))

        def alg2():
            if not self.tool:
                self.buy_tool()
            else:
                while self.money // 10 > 0:
                    self.tool -= 1
                    self.money -= 50
                    self.products.append(Item('#b24bf3', 'halfmoon', self))
                while self.money // 10 > 0:
                    if self.tool:
                        self.tool -= 1
                        self.money -= 10
                        self.products.append(Item('#3e37ff', 'halfmoon', self))
                    else:
                        if not self.buy_tool():
                            self.tool -= 1
                            self.money -= 10
                            self.products.append(Item('#3e37ff', 'halfmoon', self))

        r = random.choice([alg1, alg2])
        r()


class NPC(Seller):
    def __init__(self, name, money):
        super().__init__(name, money)

    def alg1(self):  # Алгоритмы работы ботов
        pass

    def alg2(self):
        pass

    def alg3(self):
        pass


class Market:
    def __init__(self):
        self.showcase = []


class Item:
    def __init__(self, color, form, producer):
        self.color = color
        self.form = form
        self.producer = producer
        self.day_on_market = 0

    def count(self):
        self.day_on_market += 1


class Bot_buyer:
    def __init__(self):
        self.criteria = 0

    def purchase(self, market):
        self.count_criteria = random.randint(1, 2)
        self.criteria = [random.choice(FORM + COLOR) for x in range(self.count_criteria)]
        print(self.criteria)
        for item in market.showcase[::]:
            for criter in self.criteria:
                if criter in item.form or criter in item.color:
                    market.showcase.pop(market.showcase.index(item))
                    item.producer.money += PRICE_FORM[item.form] * PRICE_COLOR[item.color]


if __name__ == '__main__':
    man = Seller('Danila', 100)
    mk = Market()
    bb1 = Bot_buyer()
    man.buy_tool()
    man.produce('Triangle')
    man.produce('Cube')
    man.send_product_on_market(mk)
    man.send_product_on_market(mk)
    print(mk.showcase)
    bb1.purchase(mk)
    print(mk.showcase)
    print(man.money)
