import random
import pickle

import Charakter
import Inventar


class Item:
    def __init__(self, name, gewicht, wert):
        inventar.gewicht += gewicht
        self.name = name
        self.gewicht = gewicht  # TODO: Gewicht/Inventar
        self.wert = wert  # TODO: Wert/Händler
        inventar.check()


class Schwert(Item):
    def __init__(self, gewicht, wert, schaden):
        self.schaden = schaden
        Item.__init__(self, "Schwert", gewicht, wert)


class Trank(Item):
    def __init__(self, name, wert):
        Item.__init__(self, name, 1, wert)


class Gesundheitstrank(Trank):
    def __init__(self, wiederhergestellte_gesundheit):
        self.wiederhergestellte_gesundheit = wiederhergestellte_gesundheit
        Trank.__init__(self, "Gesundheitstrank", self.wiederhergestellte_gesundheit * 2)


class Erfahrungstrank(Trank):
    def __init__(self, erfahrungspunkte):
        self.erfahrungspunkte = erfahrungspunkte
        Trank.__init__(self, "Erfahrungstrank", self.erfahrungspunkte * 3)


class Feld:
    def __init__(self, gegner):
        self.gegner = gegner
        self.loot = []  # TODO: Lootingsystem/Drops/Inventar

    def print_umgebung(self):
        if len(self.gegner) == 0:
            print("Du siehst dich um, siehst aber nichts Interessantes.")
        else:
            print("Du siehst dich um und siehst:")
            for i in self.gegner:
                print(i.name)


def generate_random():
    rand = random.randint(0, 2)
    if rand == 0:
        return Feld([Charakter.Bokblin(), Charakter.Haendler()])
    if rand == 1:
        return Feld([Charakter.Oktorok(), Charakter.Bokblin()])
    if rand == 2:
        return Feld([Charakter.Bokblin(), Charakter.Oktorok(), Charakter.Moblin()])


class Map:
    def __init__(self, breite, hoehe):
        self.karte = []
        self.x = 3
        self.y = 3
        for _ in range(breite):
            felder = []
            for _ in range(hoehe):
                felder.append(generate_random())
            self.karte.append(felder)

    def print_karte(self):
        self.karte[self.x][self.y].print_umgebung()

    def gegner(self):
        return self.karte[self.x][self.y].gegner

    def vorwaerts(self):
        if self.x == len(self.karte) - 1:
            print("Du siehst riesige Berge, an denen du nicht vorbeikommst")
        else:
            self.x = self.x + 1

    def rueckwaerts(self):
        if self.x == 0:
            print(
                "Du siehst Klippen, aber du kannst nicht sicher auf die andere Seite springen")
        else:
            self.x = self.x - 1

    def rechts(self):
        if self.y == len(self.karte[self.x]) - 1:
            print("Du siehst riesige Berge, an denen du nicht vorbeikommst")
        else:
            self.y = self.y + 1

    def links(self):
        if self.y == 0:
            print(
                "Du siehst Klippen, aber du kannst nicht sicher auf die andere Seite springen")
        else:
            self.y = self.y - 1


def vorwaerts(p, m):
    m.vorwaerts()
    m.print_karte()


def rechts(p, m):
    m.rechts()
    m.print_karte()


def links(p, m):
    m.links()
    m.print_karte()


def rueckwaerts(p, m):
    m.rueckwaerts()
    m.print_karte()


def speichern(p, m):
    daten = {
        "karte": map.karte,
        "x": map.x,
        "y": map.y,
        "name": spieler.name,
        "ad": spieler.ad,
        "hp": spieler.hp,
        "max_hp": spieler.max_hp,
        "ep": spieler.ep,
        "inventar": inventar.inhalt,
        "gewicht": inventar.gewicht,
        "max_gewicht": inventar.max_gewicht
    }
    datei = open("data.pickle", "wb")
    pickle.dump(daten, datei)
    datei.close()


def laden(p, m):
    datei = open("data.pickle", "rb")
    daten = pickle.load(datei)
    datei.close()
    map.karte = daten["karte"]
    map.x = daten["x"]
    map.y = daten["y"]
    spieler.name = daten["name"]
    spieler.ad = daten["ad"]
    spieler.hp = daten["hp"]
    spieler.max_hp = daten["max_hp"]
    spieler.ep = daten["ep"]
    m.print_karte()


def umschauen(p, m):
    m.print_karte()


def game_verlassen(p, m):
    print("Du hast das Spiel verlassen")
    exit(0)


def print_hilfe(p, m):
    print("Das sind alle Commands: \n")
    for command in Commands:
        print(command)


def pickup(p, m):
    pass  # TODO: pickup function + looting system


def stats(p, m):
    print("\nStats von " + p.name + ":")
    print("hp: " + str(p.hp) + "/" + str(p.max_hp))
    print("ad: " + str(p.ad))
    print("ep: " + str(p.ep) + "\n")


def print_inventar(p, m):
    for item in inventar.inhalt:
        print(item.name)
    print("\nGesamtgewicht: " + str(inventar.gewicht))


def kaempfen(p, m):
    gegner = m.gegner()
    while len(gegner) > 0:
        gegner[0].getroffen(p.ad)
        if gegner[0].ist_tot():
            p.ep += gegner[0].ep
            gegner.remove(gegner[0])
        for i in gegner:
            p.getroffen(i.ad)
            print(str(i.ad) + " hp verloren!")
    if p.hp != p.max_hp:
        print("Du hast gewonnen, bist aber verwundet und hast noch " +
              str(p.hp) + " hp übrig")
    else:
        print("Du hast gewonnen")


def ausruhen(p, m):
    p.ausruhen()


Commands = {
    'hilfe': print_hilfe,
    'stats': stats,
    'inventar': print_inventar,
    'umschauen': umschauen,
    'verlassen': game_verlassen,
    'pickup': pickup,
    'vorwärts': vorwaerts,
    'rechts': rechts,
    'links': links,
    'rückwärts': rueckwaerts,
    'kämpfen': kaempfen,
    'save': speichern,
    'load': laden,
    'ausruhen': ausruhen
}

name = input("Gib deinen Namen ein: ")
if name != "":
    spieler = Charakter.Spieler(name, 200, 100)
    map = Map(5, 5)
    inventar = Inventar.Inventar(2)
    print("(Schreibe 'hilfe' um alle Commands anzuzeigen)\n")
    while True:
        command = input(">")
        if command in Commands:
            Commands[command](spieler, map)
        else:
            print("Du drehst dich im Kreis und weißt nicht was zu tun.")
