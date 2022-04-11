import random
import Charakter
import Items
# import json
"""

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)
"""



class Feld:
    def __init__(self, gegner):
        self.gegner = gegner
        self.loot = []

    def print_umgebung(self):
        if len(self.gegner) == 0:
            print("Du siehst dich um, siehst aber nichts interessantes.")
        else:
            print("Du siehst dich um und siehst:")
            for i in self.gegner:
                print(i.name)


def generate_random():
    rand = random.randint(0, 2)
    if rand == 0:
        return Feld([Charakter.Bokblin()])
    if rand == 1:
        return Feld([Charakter.Oktorok(), Charakter.Bokblin()])
    if rand == 2:
        return Feld([Charakter.Bokblin(), Charakter.Oktorok(), Charakter.Moblin()])


class Map:
    def __init__(self, breite, höhe):
        self.karte = []
        self.x = 0
        self.y = 0
        for i in range(breite):
            felder = []
            for j in range(höhe):
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
            print("Du siehst Klippen, aber du kannst nicht sicher auf sterben andere Seite springen")
        else:
            self.x = self.x - 1

    def rechts(self):
        if self.y == len(self.karte[self.x]) - 1:
            print("Du siehst riesige Berge, an denen du nicht vorbeikommst")
        else:
            self.y = self.y + 1

    def links(self):
        if self.y == 0:
            print("Du siehst Klippen, aber du kannst nicht sicher auf sterben andere Seite springen")
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


def save(p, m):
    pass  # TODO: save function


def load(p, m):
    pass  # TODO: load function


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


def kaempfen(p, m):
    gegner = m.gegner()
    while len(gegner) > 0:
        gegner[0].getroffen(p.ad)
        if gegner[0].ist_tot():
            gegner.remove(gegner[0])
        for i in gegner:
            p.getroffen(i.ad)
            print(str(i.ad) + " hp verloren!")
    if p.hp != p.max_hp:
        print("Du hast gewonnen, bist aber verwundet und hast noch " + str(p.hp) + " hp übrig")
    else:
        print("Du hast gewonnen")


def ausruhen(p, m):
    p.ausruhen()


Commands = {
    'hilfe': print_hilfe,
    'umschauen': umschauen,
    'verlassen': game_verlassen,
    'pickup': pickup,
    'vorwärts': vorwaerts,
    'rechts': rechts,
    'links': links,
    'rückwärts': rueckwaerts,
    'kämpfen': kaempfen,
    'save': save,
    'load': load,
    'ausruhen': ausruhen
}

if __name__ == '__main__':
    name = input("Gib deinen Namen ein: ")
    if name != "":
        player = Charakter.Spieler(name, 200, 100)
        map = Map(5, 5)
        print("(Schreibe 'hilfe' um alle Commands anzuzeigen)\n")
        while True:
            command = input(">")
            if command in Commands:
                Commands[command](player, map)
            else:
                print("Du drehst dich im Kreis und weißt nicht was zu tun.")
