class Charakter:
    def __init__(self, hp, ad, name):
        self.hp = hp
        self.ad = ad
        self.name = name

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
        Charakter.__init__(self, 100, 10, "Bokblin")
        self.ep = 10


class Moblin(Charakter):
    def __init__(self):
        Charakter.__init__(self, 200, 20, "Moblin")
        self.ep = 25


class Oktorok(Charakter):
    def __init__(self):
        Charakter.__init__(self, 50, 20, "Oktorok")
        self.ep = 20


class Haendler(Charakter):
    def __init__(self):
        self.name = "Terri"
        Charakter.__init__(self, 1, 0, self.name)


class Spieler(Charakter):
    def __init__(self, name, hp, ad):
        Charakter.__init__(self, hp, ad, name)
        self.max_hp = hp
        self.ep = 0

    def sterben(self):
        exit("Du bist gestorben")

    def ausruhen(self):
        self.hp = self.max_hp
