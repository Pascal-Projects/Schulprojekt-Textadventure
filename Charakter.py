import Items as Item
import random


class Charakter:
    def __init__(self, hp, ad, drop, name):
        self.hp = hp
        self.ad = ad
        self.name = name
        self.drop = drop

    def getroffen(self, ad):
        self.hp = self.hp - ad
        if self.hp <= 0:
            self.sterben()

    def ist_tot(self):
        return self.hp <= 0

    def sterben(self):
        print(self.name + " ist gestorben")


class Bokblin(Charakter):
    def __init__(self):
        rand = random.randint(1, 3)
        if rand == 1:
            self.drop = Item.Gesundheitstrank(30)
        elif rand == 2:
            self.drop = Item.Schwert("Bokblin-Knochen", 1, 105)
        else:
            self.drop = Item.Gesundheitstrank(20)
        self.ep = 10 * rand
        Charakter.__init__(self, 100, 10, self.drop, "Bokblin")


class Moblin(Charakter):
    def __init__(self):
        rand = random.randint(1, 3)
        if rand == 1:
            self.drop = Item.Gesundheitstrank(50)
        elif rand == 2:
            self.drop = Item.Gesundheitstrank(30)
        else:
            self.drop = Item.Schwert("Antikes Schwert", 2, 140)
        self.ep = 25 * rand
        Charakter.__init__(self, 200, 20, self.drop, "Moblin")


class Oktorok(Charakter):
    def __init__(self):
        rand = random.randint(1, 4)
        if rand == 1:
            self.drop = Item.Erfahrungstrank(100)
        elif rand == 2:
            self.drop = Item.Schwert("Ritterschwert", 2, 126)
        elif rand == 3:
            self.drop = Item.Schwert("Soldatenschwert", 2, 114)
        else:
            self.drop = Item.Gesundheitstrank(100)
        self.ep = 20 * rand
        Charakter.__init__(self, 50, 20, self.drop, "Oktorok")


class Leune(Charakter):
    def __init__(self):
        self.drop = []
        rand = random.randint(1, 2)
        if rand == 1:
            self.drop = Item.Gesundheitstrank(200)
        elif rand == 2:
            self.drop = Item.Schwert("Leunenschwert", 3, 124)
        else:
            self.drop = Item.Erfahrungstrank(1000)
        self.ep = 100 * rand
        Charakter.__init__(self, 500, 50, self.drop, "Leune")


class Waechter(Charakter):
    def __init__(self):
        self.drop = []
        self.ep = 350
        Charakter.__init__(self, 500, 40, self.drop, "Wächter")


class Krog(Charakter):
    def __init__(self):
        Charakter.__init__(self, 1, None, None, "Krog")


class Maronus(Charakter):
    def __init__(self):
        Charakter.__init__(self, 1, None, None, "Maronus")


class Spieler(Charakter):
    def __init__(self, name, hp, ad, ap):
        self.max_hp = hp
        self.rubine = 0
        self.ep = 0
        self.level = 0
        self.start_ad = ad
        self.ad = ad
        self.ap = ap
        Charakter.__init__(self, hp, self.ad, None, name)
        self.levellist = [10, 25, 50, 75, 100, 200, 300, 400, 500, 600]

    def sterben(self):
        exit("Du bist gestorben")

    def ausruhen(self):
        self.hp = self.max_hp

    def nextlevel(self):
        if self.ep >= self.levellist[self.level]:
            return True

    def levelup(self):
        if self.nextlevel():
            self.ep -= self.levellist[self.level]
            self.level += 1
            print("Level up erfolgreich")
            self.max_hp += 15
            self.ad += 5
            self.start_ad += 5
            print("Dein neues Level: " + str(self.level))
        else:
            print("Du besitzt nicht genug Ehrfahrungspunkte")
