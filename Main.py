import random
import pickle
import math

import Charakter
import Inventar
import Items


class Haendler(Charakter.Charakter):
    def __init__(self):
        Charakter.Charakter.__init__(self, 1, 0, None, "Terri")
        self.artikel = []
        loop = random.randint(1, 3)
        for i in range(loop):
            rand = random.randint(1, 2)
            if rand == 1:
                randartikel = random.randint(1, 2)
                if randartikel == 1:
                    self.artikel.append(Items.Erfahrungstrank(25))
                else:
                    self.artikel.append(Items.Erfahrungstrank(50))
            else:
                randartikel = random.randint(1, 2)
                if randartikel == 1:
                    self.artikel.append(Items.Gesundheitstrank(25))
                else:
                    self.artikel.append(Items.Gesundheitstrank(50))

    def kaufen(self):  # TODO: kaufen
        print("Was willst du kaufen?")
        counter = 1
        for item in self.artikel:
            if item.name == "Erfahrungstrank":
                print(str(counter) + ". " + str(item.name) +
                      " (Erfahrungspunkte: " + str(item.erfahrungspunkte) + ", Wert: " + str(item.wert) + " Münzen )")
            elif item.name == "Gesundheitstrank":
                print(str(counter) + ". " + str(item.name) +
                      " (Wiederherstellende Gesundheit: " + str(item.wiederhergestellte_gesundheit) + ", Wert: " + str(item.wert) + " Münzen )")
            counter += 1
        item = input(
            "Gib die Zahl des Items an, welches du kaufen willst: \n>>>")
        if item == "":
            print("Bitte gib ein Item an.\n>>>")
        else:
            if int(item) > 0 and int(item) <= len(self.artikel):
                if spieler.muenzen >= self.artikel[int(item)-1].wert:
                    inventar.traenke.append(self.artikel[int(item)-1])
                    inventar.gewicht += self.artikel[int(item)-1].gewicht
                    spieler.muenzen -= self.artikel[int(item)-1].wert
                    del self.artikel[int(item)-1]
                else:
                    print("Du besitzt nicht genug Münzen.")
            else:
                print("Bitte gib eine gültige Zahl an.")

    def verkaufen(self):
        print("Was willst du verkaufen?")
        counter = 1
        for item in inventar.traenke:
            if item.name == "Erfahrungstrank":
                print(str(counter) + ". " + str(item.name) +
                      " (Erfahrungspunkte: " + str(item.erfahrungspunkte) + ", Wert: " + str(item.wert) + " Münzen )")
            elif item.name == "Gesundheitstrank":
                print(str(counter) + ". " + str(item.name) +
                      " (Wiederherstellende Gesundheit: " + str(item.wiederhergestellte_gesundheit) + ", Wert: " + str(item.wert) + " Münzen )")
            counter += 1
        item = input(
            "Gib die Zahl des Items an, welches du verkaufen willst: \n>>>")
        if item == "":
            print("Bitte gib ein Item an.\n>>>")
        else:
            if int(item) > 0 and int(item) <= len(inventar.traenke):
                spieler.muenzen += inventar.traenke[int(item)-1].wert
                inventar.gewicht -= inventar.traenke[int(item)-1].gewicht
                del inventar.traenke[int(item)-1]


class Feld:
    def __init__(self, gegner, haendler):
        self.gegner = gegner
        self.haendler = haendler
        self.loot = []

    def kaufen(self):
        if len(self.gegner) == 0:
            self.haendler.kaufen()
        else:
            print(str(self.haendler.name) +
                  " hat Angst vor den Gegner auf diesem Feld und will deswegen nichts verkaufen.")

    def verkaufen(self):
        if len(self.gegner) == 0:
            self.haendler.verkaufen()
        else:
            print(str(self.haendler.name) +
                  " hat Angst vor den Gegner auf diesem Feld und will deswegen nichts von dir kaufen.")

    def print_umgebung(self):
        if len(self.gegner) == 0 and self.haendler == None and len(self.loot) == 0:
            print("Du siehst dich um, siehst aber nichts Interessantes.")
        else:
            print("Du siehst dich um und siehst:\n")
            if len(self.gegner) != 0:
                print("Gegner: ")
                for i in self.gegner:
                    print("• " + i.name)
                print("")
            if len(self.loot) != 0:
                print("Loot: ")
                for i in self.loot:
                    print("• " + i.name)
                print("")
            if self.haendler != None:
                if len(self.gegner) != 0:
                    print(str(self.haendler.name) +
                          ", der Händler, versteckt sich vor Gegnern.")
                    print("Du kannst allerdings nur mit " + str(self.haendler.name) +
                          " handeln, wenn es keiner Gegner auf diesem Feld gibt")
                else:
                    print(str(self.haendler.name) +
                          ", den Händler, der dich begrüßt.")


def generate_random():
    gegner = [Charakter.Bokblin()]
    loop = random.randint(1, 3)
    for i in range(loop):
        rand = random.randint(1, 2)
        if rand == 1:
            gegner.append(Charakter.Bokblin())
        rand = random.randint(1, 4)
        if rand == 1:
            gegner.append(Charakter.Oktorok())
        rand = random.randint(1, 5)
        if rand == 1:
            gegner.append(Charakter.Moblin())
        rand = random.randint(1, 20)
        if rand == 1:
            gegner.append(Charakter.Leune())
    rand = random.randint(1, 5)
    if rand == 1:
        return Feld(gegner, Haendler())
    else:
        return Feld(gegner, None)


class Map:
    def __init__(self, breite, hoehe):
        self.karte = []
        self.x = math.floor(breite/2)
        self.y = math.floor(hoehe/2)
        for i in range(breite):
            felder = []
            for i in range(hoehe):
                felder.append(generate_random())
            self.karte.append(felder)

    def kaufen(self):
        self.karte[self.x][self.y].kaufen()

    def verkaufen(self):
        self.karte[self.x][self.y].verkaufen()

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
        "traenke": inventar.traenke,
        "gewicht": inventar.gewicht,
        "max_gewicht": inventar.max_gewicht,
        "muenzen": inventar.muenzen,
    }
    dateiname = input("Dateiname: \n>>>")
    datei = open(dateiname + ".pickle", "wb")
    pickle.dump(daten, datei)
    datei.close()


def laden(p, m):
    dateiname = input("Dateiname: \n>>>")
    datei = open(dateiname + ".pickle", "rb")
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
    inventar.gewicht = daten["gewicht"]
    inventar.max_gewicht = daten["max_gewicht"]
    inventar.traenke = daten["traenke"]
    inventar.muenzen = daten["muenzen"]
    m.print_karte()


def aufheben(p, m):
    if inventar.gewicht < inventar.max_gewicht:
        if len(m.karte[m.x][m.y].loot) > 0:
            print("Was willst du aufheben?")
            counter = 1
            for item in m.karte[m.x][m.y].loot:
                if item.name == "Erfahrungstrank":
                    print(str(counter) + ". " + str(item.name) +
                          " (Erfahrungspunkte: " + str(item.erfahrungspunkte) + ")")
                elif item.name == "Gesundheitstrank":
                    print(str(counter) + ". " + str(item.name) +
                          " (Wiederherstellende Gesundheit: " + str(item.wiederhergestellte_gesundheit) + ")")
                counter += 1
            item = input(
                "Gib die Zahl des Items an, welches du aufheben willst: \n>>>")
            if item == "":
                print("Bitte gib ein Item an.\n>>>")
            else:
                if int(item) > 0 and int(item) <= len(m.karte[m.x][m.y].loot):
                    inventar.traenke.append(
                        m.karte[m.x][m.y].loot[int(item)-1])
                    inventar.gewicht += m.karte[m.x][m.y].loot[int(
                        item)-1].gewicht
                    del m.karte[m.x][m.y].loot[int(item)-1]
                else:
                    print("Bitte gib eine gültige Zahl an.")
        else:
            print("Es liegt nichts auf dem Feld.")
    else:
        print("Dein Inventar ist voll. Benutze ein Item oder werfe es weg um ein neues aufzuheben.")


def benutzen(p, m):
    if len(inventar.traenke) > 0:
        print("Welches Item willst du einsetzen?")
        counter = 1
        for item in inventar.traenke:
            print(str(counter) + ". " + str(item.name))
            counter += 1
        item = input(
            "Gib die Zahl des Items an, welches du benutzen willst: \n>>>")
        if item == "":
            print("Bitte gib ein Item an.\n>>>")
        else:
            if int(item) > 0 and int(item) <= len(inventar.traenke):
                if inventar.traenke[int(item)-1].name == "Erfahrungstrank":
                    spieler.ep += inventar.traenke[int(item) -
                                                   1].erfahrungspunkte
                elif inventar.traenke[int(item)-1].name == "Gesundheitstrank":
                    if spieler.hp + inventar.traenke[int(item)-1].wiederhergestellte_gesundheit <= spieler.max_hp:
                        spieler.hp += inventar.traenke[int(item) -
                                                       1].wiederhergestellte_gesundheit
                    else:
                        print("Es würden " + str((spieler.hp + inventar.traenke[int(
                            item)-1].wiederhergestellte_gesundheit - spieler.max_hp)) + " hp verschwendet werden.")
                        x = input("Trotzdem fortfahren? (ja/nein)\n>>>")
                        if x.lower() == "ja":
                            spieler.hp = spieler.max_hp
                inventar.gewicht -= inventar.traenke[int(item)-1].gewicht
                del inventar.traenke[int(item)-1]
            else:
                print("Bitte gib eine gültige Zahl an.")
    else:
        print("Dein Inventar ist leer.")


def wegwerfen(p, m):
    print("Welches Item willst du wegwerfen?")
    counter = 1
    for item in inventar.traenke:
        print(str(counter) + ". " + str(item.name))
        counter += 1
    item = input(
        "Gib die Zahl des Items an, welches du benutzen willst: \n>>>")
    if item == "":
        print("Bitte gib ein Item an.\n>>>")
    else:
        if int(item) > 0 and int(item) <= len(inventar.traenke):
            m.karte[m.x][m.y].loot.append(inventar.traenke[int(item)-1])
            inventar.gewicht -= inventar.traenke[int(item)-1].gewicht
            inventar.traenke.pop(int(item)-1)


def umschauen(p, m):
    m.print_karte()


def game_verlassen(p, m):
    print("Du hast das Spiel verlassen")
    exit(0)


def print_hilfe(p, m):
    print("Das sind alle Commands: \n")
    for command in Commands:
        print(command)


def stats(p, m):
    print("\nStats von " + p.name + ":")
    print("hp: " + str(p.hp) + "/" + str(p.max_hp))
    print("ad: " + str(p.ad))
    print("ep: " + str(p.ep))
    print("Inventarbenutzung: " +
          str((100 / inventar.max_gewicht) * inventar.gewicht) + "%")
    print("Münzen: " + str(p.muenzen) + "\n")


def print_inventar(p, m):
    print("\nInventar von " + p.name + ":")
    for item in inventar.traenke:
        if item.name == "Erfahrungstrank":
            print(str(item.name) +
                  " (Erfahrungspunkte: " + str(item.erfahrungspunkte) + ", Wert: " + str(item.wert) + " Münzen )")
        elif item.name == "Gesundheitstrank":
            print(str(item.name) +
                  " (Wiederherstellende Gesundheit: " + str(item.wiederhergestellte_gesundheit) + ", Wert: " + str(item.wert) + " Münzen )")
    print("\nGesamtgewicht: " + str(inventar.gewicht))


def kaempfen(p, m):
    gegner = m.gegner()
    while len(gegner) > 0:
        gegner[0].getroffen(p.ad)
        if gegner[0].ist_tot():
            p.ep += gegner[0].ep
            m.karte[m.x][m.y].loot.append(gegner[0].drop)
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


def kaufen(p, m):
    m.kaufen()


def verkaufen(p, m):
    m.verkaufen()


Commands = {
    "hilfe": print_hilfe,
    "stats": stats,
    "inventar": print_inventar,
    "aufheben": aufheben,
    "benutzen": benutzen,
    "wegwerfen": wegwerfen,
    "umschauen": umschauen,
    "verlassen": game_verlassen,
    "vorwärts": vorwaerts,
    "rechts": rechts,
    "links": links,
    "rückwärts": rueckwaerts,
    "kämpfen": kaempfen,
    "save": speichern,
    "load": laden,
    "ausruhen": ausruhen,
    "kaufen": kaufen,
    "verkaufen": verkaufen,
}

name = input("Gib deinen Namen ein: ")
if name != "":
    spieler = Charakter.Spieler(name, 200, 100)
    map = Map(5, 5)
    inventar = Inventar.Inventar(5)
    print("(Schreibe 'hilfe' um alle Commands anzuzeigen)\n")
    map.print_karte()
    while True:
        command = input(">")
        if command in Commands:
            Commands[command](spieler, map)
        else:
            print("Du drehst dich im Kreis und weißt nicht was zu tun.")


# TODO: Alles auf alle Items optimieren
