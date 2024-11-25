import pygame

import logic

pygame.init()
screen = pygame.display.set_mode((610, 800))
done = False
image_tool = pygame.image.load('../images/tool.jpg').convert_alpha()
image_tool = pygame.transform.scale(image_tool, (40, 40))
image_money = pygame.image.load('../images/money.png').convert_alpha()
image_money = pygame.transform.scale(image_money, (40, 40))
image_bot1 = pygame.image.load('../images/b4.png').convert_alpha()
image_bot1 = pygame.transform.scale(image_bot1, (40, 40))


class Seller_Interface(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        pygame.draw.polygon(screen, '#70EDF4',
                            [[5, 5], [5, 205], [10, 205], [17, 196], [22, 205], [405, 205], [405, 5]],
                            5)
        pygame.draw.lines(screen, '#70EDF4', 'True', [[5, 100], [405, 100]], 5)
        pygame.draw.rect(screen, '#70EDF4', (278, 338, 44, 44), 2)

        pygame.draw.polygon(screen, '#70EDF4',
                            [[5, 405], [5, 705], [405, 705], [405, 405]],
                            5)
        pygame.draw.polygon(screen, '#70EDF4',
                            [[420, 5], [420, 705], [600, 705], [600, 5]],
                            5)
        f1 = pygame.font.Font(None, 30)
        text_strategy = f1.render('Ваша стратегия', True, '#70EDF4')
        screen.blit(text_strategy, (430, 20))
        pygame.draw.polygon(screen, '#70EDF4',
                            [[5, 720], [5, 780], [600, 780], [600, 720]],
                            5)
        # image = pygame.image.load('images/gui1.jpg').convert_alpha()
        # cropped = pygame.Surface((400, 200))
        # cropped.blit(image, (0, 0), (480, 90, 880, 300))
        # screen.blit(cropped, (0, 0))


class Buttons(pygame.sprite.Sprite):
    def __init__(self, group, color, chord_x, chord_y, form, text='', size_x=40, size_y=40, id=1):
        super().__init__(group)
        self.id = id
        self.cord_x = chord_x
        self.cord_y = chord_y
        self.form = form
        self.color = color
        self.text_btn = fb.render(f'{text}', True, '#70EDF4')
        self.text = text
        self.rect = pygame.Rect((chord_x, chord_y, size_x, size_y))
        if self.form == 'square' or self.form is None:
            pygame.draw.rect(screen, color, self.rect)
        elif self.form == 'triangle':
            pygame.draw.polygon(screen, self.color, [[self.cord_x, self.cord_y], [self.cord_x + size_x, self.cord_y],
                                                     [self.cord_x + size_x // 2, self.cord_y + size_y]])
        elif self.form == 'romb':
            pygame.draw.polygon(screen, self.color,
                                [[self.cord_x + size_x // 2, self.cord_y], [self.cord_x, self.cord_y + size_y // 2],
                                 [self.cord_x + size_x // 2, self.cord_y + size_y],
                                 [self.cord_x + size_x, self.cord_y + size_y // 2]])
        elif self.form == 'circle':
            pygame.draw.circle(screen, self.color, (self.cord_x + size_x // 2, self.cord_y + size_y // 2), size_x // 2)
        elif self.form == 'star':
            pygame.draw.polygon(screen, self.color,
                                [(self.cord_x + 20, self.cord_y), (self.cord_x + 12, self.cord_y + 10),
                                 (self.cord_x, self.cord_y + 10), (self.cord_x + 7, self.cord_y + 20),
                                 (self.cord_x + 3, self.cord_y + 35), (self.cord_x + 20, self.cord_y + 27),
                                 (self.cord_x + 37, self.cord_y + 35), (self.cord_x + 33, self.cord_y + 20),
                                 (self.cord_x + 40, self.cord_y + 10), (self.cord_x + 28,
                                                                        self.cord_y + 10)])
        elif self.form == 'halfmoon':
            pygame.draw.circle(screen, self.color, (self.cord_x + size_x // 2, self.cord_y + size_y // 2), size_x // 2)
            pygame.draw.circle(screen, 'black', (self.cord_x + size_x * 0.6 // 2, self.cord_y + size_y // 2),
                               size_x * 0.45)
        screen.blit(self.text_btn, (self.cord_x + 13, self.cord_y + 13))
        self.image_tool = pygame.image.load('../images/tool.jpg').convert_alpha()
        self.image_tool = pygame.transform.scale(self.image_tool, (40, 40))

        # отрисовка кнопок

    def click(self):
        global GLOBAL_CHOISE
        GLOBAL_CHOISE = self.color

    def re_render(self):
        pygame.draw.rect(screen, 'black', self.rect)
        if self.form == 'square' or self.form is None:
            pygame.draw.rect(screen, self.color, self.rect)
        elif self.form == 'triangle':
            pygame.draw.polygon(screen, self.color, [[self.cord_x, self.cord_y], [self.cord_x + 40, self.cord_y],
                                                     [self.cord_x + 20, self.cord_y + 40]])
        elif self.form == 'romb':
            pygame.draw.polygon(screen, self.color, [[self.cord_x + 20, self.cord_y], [self.cord_x, self.cord_y + 20],
                                                     [self.cord_x + 20, self.cord_y + 40],
                                                     [self.cord_x + 40, self.cord_y + 20]])
        elif self.form == 'circle':
            pygame.draw.circle(screen, self.color, (self.cord_x + 20, self.cord_y + 20), 20)
        elif self.form == 'star':
            pygame.draw.polygon(screen, self.color,
                                [(self.cord_x + 20, self.cord_y), (self.cord_x + 12, self.cord_y + 10),
                                 (self.cord_x, self.cord_y + 10), (self.cord_x + 7, self.cord_y + 20),
                                 (self.cord_x + 3, self.cord_y + 35), (self.cord_x + 20, self.cord_y + 27),
                                 (self.cord_x + 37, self.cord_y + 35), (self.cord_x + 33, self.cord_y + 20),
                                 (self.cord_x + 40, self.cord_y + 10), (self.cord_x + 28, self.cord_y + 10)])
        elif self.form == 'halfmoon':
            pygame.draw.circle(screen, self.color, (self.cord_x + 20, self.cord_y + 20), 20)
            pygame.draw.circle(screen, 'black', (self.cord_x + 26, self.cord_y + 20), 15)
        screen.blit(self.text_btn, (self.cord_x + 13, self.cord_y + 13))
        pygame.draw.rect(screen, '#70EDF4', (278, 338, 44, 44), 2)

    def tool(self):
        screen.blit(self.image_tool, (self.cord_x, self.cord_y))


class Inventory_product(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        # отрисовка интерфейса готовых изделий


class Inventory_blank(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        # отрисовка интерфейса заготовок


class Showcase(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        # отрисовка интерфейса заготовок

    def update(self):
        pass  # отрисовка витрины после добавления в нее товаров


class Timer(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        # отрисовка таймера

    def update(self):
        pass  # отрисовка таймера времени


class Money(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        # отрисовка денег

    def update(self):
        pass  # проверка денег у класса и вывод цифры на экран


screen.fill('black')
"""
Создаем игрока
"""


def render_form(item, k, j=0):
    Buttons(buttons, item.color, 20 + (50 * k), 40 + (40 * j), item.form)


def render_showcase(item, k, j=0, name=''):
    Buttons(buttons, item.color, 20 + (50 * k), 420 + (40 * j), item.form)
    Buttons(buttons, item.color, 430 + (25 * k), 40 + (25 * j), item.form, size_x=20, size_y=20)


def render_tool():
    pygame.draw.rect(screen, 'black', (40, 140, 200, 50))
    for i in range(man.tool):
        screen.blit(image_tool, (40 * (i + 1), 140))
    screen.blit(image_money, (10, 340))
    f1 = pygame.font.Font(None, 30)
    pygame.draw.rect(screen, 'black', (50, 350, 70, 50))
    text_money = f1.render(f'{man.money}', True, '#70EDF4')
    screen.blit(text_money, (60, 355))
    k = 0
    pygame.draw.rect(screen, 'black', (20, 40, 280, 40))
    for elm in man.products:
        render_form(elm, k)
        k += 1


def render_market(markt):
    k, j = 0, 0
    pygame.draw.rect(screen, 'black', (10, 410, 380, 280))
    for elem in markt.showcase:
        render_showcase(elem, k, j)
        k += 1
        if k == 5:
            j += 1
            k = 0


man = logic.Seller('Name', 100)
market = logic.Market()
render_tool()
bot_b = logic.Bot_buyer()

bot_p1 = logic.Seller('bot1', 100)
bot_p2 = logic.Seller('bot2', 100)
bot_p3 = logic.Seller('bot3', 100)
bot_p4 = logic.Seller('bot4', 100)
bot_p5 = logic.Seller('bot5', 100)
bot_p6 = logic.Seller('bot6', 100)

for i in range(6):
    screen.blit(image_bot1, (20 + 60 * i, 730))
# def game_ini():
#     pass


"""
создаем группы спрайтов
"""

f1 = pygame.font.Font(None, 30)
fb = pygame.font.Font(None, 20)
text1 = f1.render('Выберите', True, '#70EDF4')
text2 = f1.render('    цвет', True, '#70EDF4')
text3 = f1.render('   форму', True, '#70EDF4')
inventory_text = f1.render('Готовые изделия', True, '#70EDF4')
tool_text = f1.render('Инструменты', True, '#70EDF4')
text_produce = f1.render('Получится:', True, '#70EDF4')
screen.blit(text1, (30, 220))
screen.blit(text2, (30, 240))
screen.blit(text1, (30, 280))
screen.blit(text3, (30, 300))
screen.blit(inventory_text, (10, 10))
screen.blit(tool_text, (10, 110))
screen.blit(text_produce, (160, 350))

interface = pygame.sprite.Group()
buttons = pygame.sprite.Group()
# products = pygame.sprite.Group()
# blanks = pygame.sprite.Group()
# showcases = pygame.sprite.Group()
#
first_player = Seller_Interface(interface)
btn_red = Buttons(buttons, '#b22222', 230, 220, None, '30')
btn_green = Buttons(buttons, '#0a7e07', 180, 220, None, '20')
btn_blue = Buttons(buttons, '#3e37ff', 130, 220, None, '10')
btn_yellow = Buttons(buttons, '#fded00', 280, 220, None, '40')
btn_purple = Buttons(buttons, '#b24bf3', 330, 220, None, '50')
btn_CHOISE = Buttons(buttons, 'black', 280, 340, 'square')

btn_tool = Buttons(buttons, 'black', 330, 340, None)
btn_buy_tool = Buttons(buttons, 'red', 310, 112, None, size_x=80, size_y=80, id=2, text='Купить')
btn_sell_products = Buttons(buttons, 'red', 310, 12, None, size_x=80, size_y=80, id=3, text='продать')
btn_next_day = Buttons(buttons, 'red', 400, 740, None, size_x=160, size_y=30, id=4, text='следующий день')

btn_triangle = Buttons(buttons, 'white', 230, 280, 'triangle')
btn_romb = Buttons(buttons, 'white', 180, 280, 'romb')
btn_circle = Buttons(buttons, 'white', 130, 280, 'circle')
btn_star = Buttons(buttons, 'white', 280, 280, 'star')
btn_halfmoon = Buttons(buttons, 'white', 330, 280, 'halfmoon')

btn_tool.tool()


# surf = pygame.Surface((410, 800))
# screen.blit(surf, (0, 0))


def check_click():
    for elem in buttons:
        if elem.rect.collidepoint(pygame.mouse.get_pos()):
            x, y = pygame.mouse.get_pos()
            if (130 < x < 370) and (220 < y < 260):
                btn_CHOISE.text_btn = elem.text_btn
                btn_CHOISE.text = elem.text
                btn_CHOISE.color = elem.color
                koef = {'romb': 1.5, 'triangle': 1.7, 'circle': 1.9, 'star': 2.1, 'halfmoon': 2.3, '': 1, 'square': 1}
                btn_CHOISE.text_btn = fb.render(f'{str(int(float(elem.text) * koef[btn_CHOISE.form]))}', True,
                                                '#70EDF4')
                btn_CHOISE.re_render()
            elif (130 < x < 370) and (280 < y < 320):
                if btn_CHOISE.text != '':
                    btn_CHOISE.form = elem.form
                    koef = {'romb': 1.5, 'triangle': 1.7, 'circle': 1.9, 'star': 2.1, 'halfmoon': 2.3, '': 1,
                            'square': 1}
                    btn_CHOISE.text_btn = fb.render(f'{str(int(float(btn_CHOISE.text) * koef[elem.form]))}', True,
                                                    '#70EDF4')
                    btn_CHOISE.re_render()
            elif elem.id == 2:
                if not man.buy_tool():
                    pass
            elif elem.id == 3:
                if not man.send_product_on_market(market):
                    pass
                else:
                    render_market(market)
            elif elem.id == 4:
                print('sssss')
                for elem in [bot_p1, bot_p2, bot_p3, bot_p4, bot_p5, bot_p6]:
                    elem.strategy()
                    elem.send_product_on_market(market)
                bot_b.purchase(market)
            else:
                man.produce(btn_CHOISE)
                btn_CHOISE.color = 'black'
                btn_CHOISE.form = 'square'
                btn_CHOISE.text = '0'
                btn_CHOISE.text_btn = fb.render('', True, 'black')
                btn_CHOISE.re_render()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_click()
    pressed = pygame.key.get_pressed()
    render_tool()
    render_market(market)

    # interface.draw(screen)  # отрисовать интерфейс
    # buttons.draw(screen)  # отрисовать кнопки
    # products.draw(screen)  # отрисовать инвентарь готовых изделий
    # blanks.draw(screen)  # отрисовать инвентарь заготовок
    # showcases.draw(screen)  # отрисовать витрину сейчас

    pygame.display.flip()
