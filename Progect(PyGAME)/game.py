import os
import pygame
from random import choice
import sqlite3
import random

pygame.init()
size = width, height = 1000, 606
screen = pygame.display.set_mode(size)
summsolnz = 1000
zombi = pygame.sprite.Group()
fon = pygame.sprite.Group()
carts = pygame.sprite.Group()
plants = pygame.sprite.Group()
iadra = pygame.sprite.Group()
lopata = pygame.sprite.Group()
solnze = pygame.sprite.Group()
kosilka = pygame.sprite.Group()
kolvoz = 0
con = sqlite3.connect("levelcarts.db")
cur = con.cursor()
i = cur.execute("Select name from cartslevels WHERE id=?", (1,)).fetchall()
i = i[0][0]
b = cur.execute("Select level from cartslevels WHERE name=?", (i,)).fetchall()
d = cur.execute("Select carts from cartslevels WHERE name=?", (i,)).fetchall()
d = d[0][0].split(">")
b = b[0][0]
if b == 1:
    spisokzomb = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
if b == 2:
    spisokzomb = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
if b == 3:
    spisokzomb = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3]
if b == 3:
    spisokzomb = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3]
if b == 4:
    spisokzomb = [0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 2, 3]
if b == 5:
    spisokzomb = [0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 3, 3]
if b == 6:
    spisokzomb = [0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 3, 3, 3, 3]
if b == 7:
    spisokzomb = [0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4]
if b == 8:
    spisokzomb = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4]
if b == 9:
    spisokzomb = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 4, 3, 5]
if b == 10:
    spisokzomb =  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 4, 3, 5, 5]
con.commit()
con.close()
done = False
clock = pygame.time.Clock()
konlist = [[78, 12], [132, 12], [186, 12], [241, 12], [295, 12], [347, 12]]
linii = []

def dengi(a, b):
    global summsolnz
    if a == 1:
        summsolnz += b
    else:
        summsolnz -= b

def dele(a):
    global kolvoz
    global linii
    print(a)
    del linii[linii.index(a)]
    kolvoz -= 1

class Carts(pygame.sprite.Sprite):
    def __init__(self, group, pos, pict):
        super().__init__(group)
        x = pos[0]
        y = pos[1]
        self.image = load_image(pict, "carts")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.konlist = [[78, 12], [132, 12], [186, 12], [241, 12], [295, 12], [347, 12]]
        self.pict = pict.split(".")[0]
        self.chek1 = 0
        self.up = 0
        self.kolvo = 10
        self.n = 0
        if pict == "KUSHA.png":
            self.price = 150
            self.time = 2300
        if pict == "scoro.png":
            self.price = 200
            self.time = 2500
        if pict == "IAGODA.png":
            self.price = 150
            self.time = 5000
        if pict == "holod.png":
            self.price = 10
            self.time = 2500
        if pict == "NORMAL.png":
            self.price = 100
            self.time = 1000
        if pict == "POTATO.png":
            self.price = 50
            self.time = 3100
        if pict == "CVET.png":
            self.price = 50
            self.time = 1000
        if pict == "CVET.png":
            self.price = 50
            self.time = 1000
        self.timer = 0
        self.clock1 = pygame.time.Clock()

    def update(self, args):
        m = self.clock1.tick()
        self.timer = m + self.timer
        if self.up == 1:
            pygame.draw.rect(screen, (0, 0, 0, 255),
                             (self.rect.x, self.rect.y + self.n * 70 // self.kolvo, 50, 70 - self.n * 70 // self.kolvo), 0)
        if args[1] == 1 and self.chek1 == 1:
            if self.rect.x > 95 and self.rect.x < 960 and self.rect.y > 90 and self.rect.y < 606:
                x = (self.rect.x - 95) // 100 * 100 + 95
                y = (self.rect.y - 90) // 100 * 100 + 90
                if self.pict == "CVET":
                    Rust(plants, "podsolnux.png", load_image("podsolnux.png", "animashionspr"), 8, 1, x, y, (self.rect.y - 90) // 100)
                if self.pict == "NORMAL":
                    Rust(plants, "normalan.png", load_image("normalan.png", "animashionspr"), 8, 1, x, y, (self.rect.y - 90) // 100)
                if self.pict == "POTATO":
                    Rust(plants, "cart.png", load_image("cart.png", "animashionspr"), 1, 1, x, y, (self.rect.y - 90) // 100)
                if self.pict == "holod":
                    Rust(plants, "holod.png", load_image("holod.png", "animashionspr"), 8, 1, x, y,
                         (self.rect.y - 90) // 100)
                if self.pict == "KUSHA":
                    Kusha(plants, "kussha.png", load_image("kussha.png", "animashionspr"), 9, 1, x, y, 1)
                if self.pict == "IAGODA":
                    Rust(plants, "iagoda.png", load_image("iagoda.png", "animashionspr"), 6, 1, x, y,
                         (self.rect.y - 90) // 100)
                if self.pict == "scoro":
                    Rust(plants, "scorastrel.png", load_image("scorastrel.png", "animashionspr"), 5, 1, x, y,
                         (self.rect.y - 90) // 100)
                if self.pict == "ships":
                    Rust(plants, "ships.png", load_image("ships.png", "animashionspr"), 5, 1, x, y,
                         (self.rect.y - 90) // 100)
                if self.pict == "scoro":
                    Rust(plants, "scorastrel.png", load_image("scorastrel.png", "animashionspr"), 5, 1, x, y,
                         (self.rect.y - 90) // 100)
                self.up = 1
                k1 = self.price
                dengi(0, k1)
            self.rect.x = self.izpoz[0]
            self.rect.y = self.izpoz[1]
            self.chek1 = 0
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            if [self.rect.x, self.rect.y] in self.konlist and args[1] == 0 and self.up == 0 and args[3] >= self.price:
                self.chek1 = 1
                self.izpoz = [self.rect.x, self.rect.y]
        if self.chek1 == 1:
            self.rect.x = args[0].pos[0]
            self.rect.y = args[0].pos[1]
        if self.timer > self.time and self.up == 1:
            self.timer = 0
            self.n += 1
        if self.n == self.kolvo:
            self.up = 0
            self.n = 0


class Rust(pygame.sprite.Sprite):
    def __init__(self, group, pict, sheet, columns, rows, x, y, k, hp=-1):
        super().__init__(group)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.chek1 = 0
        self.pict = pict
        self.image = self.frames[self.cur_frame]
        self.rect.x = x
        self.rect.y = y
        if hp == -1:
            print(self.pict)
            if pict == "cart.png":
                self.hp = 500
            else:
                self.hp = 100
        else:
            self.hp = hp
        self.linia = k
        self.clock1 = pygame.time.Clock()
        self.timer = 0
        self.timer2 = 0
        if pict == "scorastrel.png":
            self.time = 3500
        else:
            self.time = 5000
        self.chek = 0
        self.kolvoan = 0
        self.kolvoand = columns * rows


    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, args):
        if j7 > 500:
            if pygame.sprite.spritecollideany(self, zombi):
                self.hp -= 10
        if self.pict == "iagodaATTACK.png":
            hits = pygame.sprite.groupcollide(plants, zombi, False, False)
            for t in hits:
                if t.pict == "iagodaATTACK.png":
                    for t1 in hits[t]:
                        t1.kill()
        if j1 > 150:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
            self.kolvoan += 1
        if self.kolvoan == self.kolvoand:
            if self.pict == "iagodaATTACK.png":
                self.kill()
            if self.pict == "iagoda.png":
                Rust(plants, "iagodaATTACK.png", load_image("iagodaATTACK.png", "animashionspr"), 8, 1, self.rect.x,
                     self.rect.y,
                     (self.rect.y - 90) // 100, self.hp)
                self.kill()
            if self.pict in ["normalATTACK.png", "scorastrelATTACK.png"]:
                self.chek = 1
            self.kolvoan = 0
        self.image.set_colorkey((255, 255, 255))
        if args[0] != 0:
            self.hp -= args[0]
        if self.hp < 0 or self.hp == 0:
            self.kill()
            return 1
        if self.linia in args[1] and self.timer > self.time:
            if self.pict == "normalan.png":
                Rust(plants, "normalATTACK.png", load_image("normalATTACK.png", "animashionspr"), 3, 1, self.rect.x, self.rect.y,
                     (self.rect.y - 90) // 100, self.hp)
                self.kill()
            elif self.pict == "holod.png":
                self.chek = 1
            elif self.pict == "scorastrel.png":
                Rust(plants, "scorastrelATTACK.png", load_image("scorastrelATTACK.png", "animashionspr"), 2, 1, self.rect.x,
                     self.rect.y,
                     (self.rect.y - 90) // 100, self.hp)
                self.kill()
        if self.chek == 1:
            if self.pict == "holod.png":
                Iadro(iadra, "XOLOD.png", self.rect.x + 46, self.rect.y - 1)
            elif self.pict == "normalATTACK.png":
                Iadro(iadra, "NORMAL1.png", self.rect.x + 46, self.rect.y - 1)
                Rust(plants, "normalan.png", load_image("normalan.png", "animashionspr"), 8, 1, self.rect.x, self.rect.y,
                    (self.rect.y - 90) // 100, self.hp)
                self.kill()
            elif self.pict == "scorastrelATTACK.png":
                Iadro(iadra, "NORMAL1.png", self.rect.x + 46, self.rect.y - 1)
                Rust(plants, "scorastrel.png", load_image("scorastrel.png", "animashionspr"), 5, 1, self.rect.x,
                     self.rect.y,
                     (self.rect.y - 90) // 100, self.hp)
                self.kill()
            self.chek = 0
            self.timer = 0
        if self.pict == "podsolnux.png" and self.timer2 > 8000:
            self.timer2 = 0
            Solnce(solnze, [self.rect.x + 50, self.rect.y])
        m = self.clock1.tick()
        self.timer = m + self.timer
        self.timer2 = m + self.timer2

    def chek1(self):
        return self.pict


class Kusha(pygame.sprite.Sprite):
    def __init__(self, group, pict, sheet, columns, rows, x, y, k, zomby=0, hp=-1):
        super().__init__(group)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.chek1 = 0
        self.pict = pict
        self.image = self.frames[self.cur_frame]
        self.rect.x = x
        self.rect.y = y
        if hp == -1:
            self.hp = 100
        else:
            self.hp = hp
        self.clock1 = pygame.time.Clock()
        self.timer = 0
        self.chek = 0
        self.kolvoan = 0
        self.kolvoand = columns * rows
        self.zomby = zomby

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, args):
        self.image.set_colorkey((255, 255, 255))
        m = self.clock1.tick()
        self.timer = m + self.timer
        if j1 > 150:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
            self.kolvoan += 1
        if self.kolvoan == self.kolvoand and self.pict == "kushaATTACK.png":
            self.zomby.kill()
            Kusha(plants, "KUSHAback.png", load_image("KUSHAback.png", "animashionspr"), 1, 1, self.rect.x, self.rect.y,
                  (self.rect.y - 90) // 100, self.hp)
            self.kill()
        hits = pygame.sprite.groupcollide(plants, zombi, False, False)
        if self.pict == "kussha.png":
            for t in hits:
                if t.pict == "kussha.png":
                    Kusha(plants, "kushaATTACK.png", load_image("kushaATTACK.png", "animashionspr"), 8, 1, t.rect.x,
                          t.rect.y, ((self.rect.y - 90) // 100), hits[t][0], self.hp)
                    t.kill()
        if self.timer > 10000:
            self.timer = 0
            if self.pict == "KUSHAback.png":
                Kusha(plants, "kussha.png", load_image("kussha.png", "animashionspr"), 9, 1, self.rect.x, self.rect.y,
                      (self.rect.y - 90) // 100, self.hp)
                self.kill()

    def chek1(self):
        return self.pict



def load_image(name, k):
    fullname = os.path.join(k, name)
    return pygame.image.load(fullname).convert()


class Solnce(pygame.sprite.Sprite):
    def __init__(self, group, pos):
        super().__init__(group)
        x = pos[0]
        y = pos[1]
        self.image = load_image("solnze.png", "animashionspr")
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.znak = 1
        self.chek = 0
        self.ug = [3333, 333]
        self.o, self.o2 = 0, 0

    def update(self, args=[]):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            self.chek = 1
            self.ug = [self.rect.x, self.rect.y]
        if self.chek == 1:
            self.rect = self.rect.move((-1 * self.ug[0] // 10, -1 * self.ug[1] // 10))
            self.o += 1
        if self.o == 9 and self.chek == 1:
            self.chek = 0
            dengi(1, 25)
            self.kill()


class Fon(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = load_image("gamemain.png", "fons")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

class Iadro(pygame.sprite.Sprite):
    def __init__(self, group, pic, x, y):
        super().__init__(group)
        self.image = load_image(pic, "patron")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = pic[0]

    def update(self, a=0):
        if a != 0:
            self.kill()
        if j3 > 10:
            self.rect = self.rect.move(1, 0)
        self.image.set_colorkey((255, 255, 255))


class Zomby(pygame.sprite.Sprite):
    def __init__(self, group, sheet, columns, rows, x, y, tipe, k):
        super().__init__(group)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect.x = x
        self.rect.y = y
        self.chek = 0
        self.time = 250
        self.hp = 100
        if tipe == 0:
            self.hp = 250
        elif tipe == 1:
            self.time = 300
            self.hp = 400
        elif tipe == 2:
            self.hp = 700
        elif tipe == 3:
            self.time = 100
            self.hp = 1000
        self.timer = 0
        self.timer2 = 0
        self.chek1 = 0
        self.clock1 = pygame.time.Clock()
        self.chektime = 0
        self.y = k

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, args):
        self.image.set_colorkey((255, 255, 255))
        if self.chek1 == 1:
            self.time += 150
            self.timer2 = 0
            self.chek1 = 2
        if self.timer2 > 5000 and self.chek1 == 2:
            self.time -= 150
            self.chek1 = 0
            self.timer2 = 0
        args.append(0)
        m = self.clock1.tick()
        self.timer = m + self.timer
        self.timer2 = m + self.timer2
        if self.hp == 0 or self.hp < 0:
            dele(self.y)
            self.kill()
        if self.timer > self.time:
            self.timer = 0
            if self.chek == 0:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames)
                self.image = self.frames[self.cur_frame]
                self.rect = self.rect.move(-3, 0)
            hits2 = pygame.sprite.groupcollide(iadra, zombi, False, False)
            hits3 = pygame.sprite.groupcollide(kosilka, zombi, False, True)
            if hits2 != {}:
                for t in hits2:
                    if t.type == "X":
                        for t1 in hits2[t]:
                            if t1.chek1 == 0:
                                t1.chek1 = 1
                    t.update(1)
                    for t1 in hits2[t]:
                        t1.hp -= 50
            if hits3 != {}:
                for t in hits3:
                    t.update(1)
                    for t1 in hits3[t]:
                        dele(self.y)
        if pygame.sprite.spritecollideany(self, plants):
            self.chek = 1
        else:
            self.chek = 0


class Kosilka(pygame.sprite.Sprite):
    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = load_image("kos.png", "animashionspr")
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255, 255, 255))
        self.rect.x = x
        self.rect.y = y
        self.chek = 0

    def update(self, a=0):
        if a != 0:
            self.chek = 1
        if self.chek == 1:
            self.rect = self.rect.move(10, 0)


class Kosilka(pygame.sprite.Sprite):
    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = load_image("kos.png", "animashionspr")
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255, 255, 255))
        self.rect.x = x
        self.rect.y = y
        self.chek = 0

    def update(self, a=0):
        if a != 0:
            self.chek = 1
        if self.chek == 1:
            self.rect = self.rect.move(10, 0)



for t in range(4):
    Kosilka(kosilka, 15, 115 + t * 90)
Kosilka(kosilka, 15, 115 + 4 * 95)
for t in range(len(d)):
    Carts(carts, konlist[t], d[t])
chek = 0
Fon(fon)
clock = pygame.time.Clock()
j = 0
j1 = 0
j2 = 0
j3 = 0
j4 = 0
j5 = 0
j6 = 0
j7 = 0
time = 7000
obchtime = 0
while done == False:
    t1 = clock.tick()
    obchtime += t1
    j7 += t1
    j += t1
    j1 += t1
    j2 += t1
    j3 += t1
    j4 += t1
    j5 += t1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            carts.update([event, 0, j, summsolnz])
            solnze.update([event])
        if event.type == pygame.MOUSEBUTTONUP:
            carts.update([event, 1, j])
    fon.draw(screen)
    plants.draw(screen)
    zombi.draw(screen)
    solnze.draw(screen)
    iadra.draw(screen)
    carts.draw(screen)
    kosilka.draw(screen)
    carts.update([event, 2, j, linii])
    plants.update([0, linii, 1])
    zombi.update([0, j])
    iadra.update()
    f1 = pygame.font.SysFont("", 40)
    text1 = f1.render(str(summsolnz), 0, (0, 0, 0))
    screen.blit(text1, (20, 63))
    if obchtime < 180000 and obchtime > 170000:
        f2 = pygame.font.SysFont("", 60)
        text2 = f2.render("Скоро волна...", 0, (0, 0, 0))
        screen.blit(text2, (440, 290))
    pygame.display.flip()
    if j7 > 500:
        j7 = 0
    if j5 > 70:
        j5 = 0
        solnze.update()
        kosilka.update()
    if j3 > 10:
        j3 = 0
    if j > 1000:
        j = 0
    if j1 > 150:
        j1 = 0
    if obchtime > 180000:
        for t in range(1, 4):
            for t1 in range(5):
                x = 9 * 100 + t * 80
                y = t1 * 100 + 70
                k = t1
                tipe = random.choice(spisokzomb)
                if t == 5:
                    Zomby(zombi, load_image("zomby.png", "animashionspr"), 8, 1, x, y, spisokzomb[-1 * t1], k)
                elif tipe == 0:
                    Zomby(zombi, load_image("zomby.png", "animashionspr"), 8, 1, x, y, tipe, k)
                elif tipe == 1:
                    Zomby(zombi, load_image("zombyKONUS.png", "animashionspr"), 8, 1, x, y, tipe, k)
                elif tipe == 2:
                    Zomby(zombi, load_image("zombyVEDRO.png", "animashionspr"), 8, 1, x, y, tipe, k)
                elif tipe == 3:
                    Zomby(zombi, load_image("zombyBEG.png", "animashionspr"), 8, 1, x, y, tipe, k)
                linii.append(t1)
                kolvoz += 1
                chek = 1
    elif j2 > time and chek == 0:
        time -= 300
        j2 = 0
        k = random.choice([0, 1, 2, 3, 4])
        tipe = random.choice(spisokzomb)
        linii.append(k)
        x = 9 * 100 + 80
        y = k * 100 + 70
        if tipe == 0:
            Zomby(zombi, load_image("zomby.png", "animashionspr"), 8, 1, x, y, tipe, k)
        elif tipe == 1:
            Zomby(zombi, load_image("zombyKONUS.png", "animashionspr"), 8, 1, x, y, tipe, k)
        elif tipe == 2:
            Zomby(zombi, load_image("zombyVEDRO.png", "animashionspr"), 8, 1, x, y, tipe, k)
        elif tipe == 3:
            Zomby(zombi, load_image("zombyBEG.png", "animashionspr"), 8, 1, x, y, tipe, k)
        kolvoz += 1
    if obchtime > 18000:
        obchtime = -1000000000
    if kolvoz == 0 and chek == 1:
        pygame.quit()
        os.system('python obiavlenia.py')
pygame.quit()
