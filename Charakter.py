import Items as Item
import random


class Charakter:
    def __init__(self, hp, ad, drop, name):  # TODO: Drops
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
        rand = random.randint(1, 2)
        if rand == 1:
            self.drop = Item.Gesundheitstrank(30)
        else:
            self.drop = Item.Gesundheitstrank(20)
        self.ep = 10 * rand
        Charakter.__init__(self, 100, 10, self.drop, "Bokblin")


class Moblin(Charakter):
    def __init__(self):
        rand = random.randint(1, 2)
        if rand == 1:
            self.drop = Item.Gesundheitstrank(50)
        else:
            self.drop = Item.Gesundheitstrank(30)
        self.ep = 25 * rand
        Charakter.__init__(self, 200, 20, self.drop, "Moblin")


class Oktorok(Charakter):
    def __init__(self):
        rand = random.randint(1, 2)
        if rand == 1:
            self.drop = Item.Erfahrungstrank(100)
        else:
            self.drop = Item.Gesundheitstrank(100)
        self.ep = 20 * rand
        Charakter.__init__(self, 50, 20, self.drop, "Oktorok")


class Leune(Charakter):
    def __init__(self):
        rand = random.randint(1, 2)
        if rand == 1:
            self.drop = Item.Gesundheitstrank(200)
        else:
            self.drop = Item.Erfahrungstrank(1000)
        self.ep = 100 * rand
        Charakter.__init__(self, 500, 50, self.drop, "Leune")


class Spieler(Charakter):
    def __init__(self, name, hp, ad):
        self.max_hp = hp
        self.muenzen = 0
        self.ep = 0  # TODO: Level
        Charakter.__init__(self, hp, ad, None, name)

    def sterben(self):
        exit("Du bist gestorben")

    def ausruhen(self):
        self.hp = self.max_hp
