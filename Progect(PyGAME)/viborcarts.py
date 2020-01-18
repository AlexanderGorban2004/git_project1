import os
import pygame
from random import choice
import sqlite3


pygame.init()
size = width, height = 1000, 606
screen = pygame.display.set_mode(size)
con = sqlite3.connect("levelcarts.db")
cur = con.cursor()
i = cur.execute("Select name from cartslevels WHERE id=?", (1,)).fetchall()
i = i[0][0]
b = cur.execute("Select level from cartslevels WHERE name=?", (i,)).fetchall()
b = b[0][0]


max = 6
if b == 1:
    pict = ["CVET.png", "NORMAL.png", "IAGODA.png", "POTATO.png", "KUSHA.png"]
    max = 5
white = [255, 255, 255]
black = [0, 0, 0]
carts = pygame.sprite.Group()
fon = pygame.sprite.Group()
but = pygame.sprite.Group()
konlist = [[78, 12], [132, 12], [186, 12], [241, 12], [295, 12], [347, 12]]
a = 0
w = []
con.commit()
con.close()

def list(a1="f"):
    global konlist
    global a
    if konlist != []:
        del konlist[0]
    w.append(a1)
    a += 1

def list2(arg, a1="d"):
    global konlist
    konlist.insert(0, arg)
    global a
    a -= 1
    del w[w.index(a1)]

def save():
    con = sqlite3.connect("levelcarts.db")
    cur = con.cursor()
    n = ">".join(w)
    print(n)
    cur.execute("UPDATE cartslevels SET carts = ? WHERE name = ?", (n, i), ).fetchall()
    con.commit()
    con.close()
    pygame.quit()
    os.system('python game.py')

def load_image(name, k):
    fullname = os.path.join(k, name)
    return pygame.image.load(fullname).convert()

class Carts(pygame.sprite.Sprite):
    def __init__(self, group, pos, pict):
        super().__init__(group)
        x = pos[0]
        y = pos[1]
        self.p = pict
        self.image = load_image(pict, "carts")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.znak = 1
        self.chek = 0
        self.ug, self.ug2 = [3333, 333], [44444]
        self.o, self.o2 = 0, 0

    def update(self, args=[]):
        print(args)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            if self.rect.y < 13:
                list2([self.rect.x, self.rect.y], self.p)
                self.chek = 2
            elif args[2] < args[3]:
                self.chek = 1
                self.ug = args[1][0]
                self.ug2 = self.rect.x, self.rect.y
                list(self.p)
            else:
                print(4)
        if self.chek == 1:
            self.rect = self.rect.move((self.ug[0] - self.ug2[0]) // 10, -1 * self.ug2[1] // 10)
            self.o += 1
        elif self.chek == 2:
            self.rect = self.rect.move(-1 * (self.ug[0] - self.ug2[0]) // 10, self.ug2[1] // 10)
            self.o2 += 1
        if self.o == 9 and self.chek == 1:
            self.chek = 0
            self.o = 0
            self.rect.x, self.rect.y = self.ug
        if self.o2 == 9 and self.chek == 2:
            self.chek = 0
            self.o2 = 0
            self.rect.x, self.rect.y = self.ug2


class Fon(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = load_image("FonCarts.png", "fons")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


class Zomby(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = load_image("FonCarts.png", "fons")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


class Knopka(pygame.sprite.Sprite):
    b = load_image("pol.png", "buttons")
    image1 = load_image("pol2.png", "buttons")

    def __init__(self, group):
        super().__init__(group)
        self.image = Knopka.b
        self.rect = self.image.get_rect()
        self.rect.x = 153
        self.rect.y = 551

    def update(self, args):
        if args[1] == args[2]:
            self.image = self.image1
        else:
            self.image = self.b
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            if args[1] == args[2]:
                save()


class MainMenu(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = load_image("mainmentu.png", "buttons")
        self.rect = self.image.get_rect()
        self.rect.x = 900
        self.rect.y = 0

    def update(self, args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            pygame.quit()
            os.system('python mainmenu.py')


Knopka(but)
MainMenu(but)
n = -1
Fon(fon)
for t in pict:
    n += 1
    Carts(carts, (20 + n * 50 + n * 5, 124), t)
done = False
clock = pygame.time.Clock()
j = 0
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            carts.update([event, konlist, a, max])
            but.update([event, a, max, n, i])
    fon.draw(screen)
    carts.draw(screen)
    t1 = clock.tick()
    j += t1
    if j > 20:
        j = 0
        carts.update()
    f1 = pygame.font.SysFont("", 48)
    f2 = pygame.font.SysFont("", 48)
    text2 = f2.render("Уровень - " + str(b), 0, (255, 0, 0))
    text1 = f1.render("Доступно карточек - " + str(max), 0, (255, 0, 0))
    screen.blit(text1, (560, 50))
    screen.blit(text2, (560, 100))
    but.draw(screen)
    pygame.display.flip()
pygame.quit()