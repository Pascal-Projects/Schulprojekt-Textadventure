class Item:
    def __init__(self, name, gewicht, wert):
        self.name = name
        self.gewicht = gewicht
        self.wert = wert


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
        Trank.__init__(self, "Gesundheitstrank",
                       self.wiederhergestellte_gesundheit * 2)


class Erfahrungstrank(Trank):
    def __init__(self, erfahrungspunkte):
        self.erfahrungspunkte = erfahrungspunkte
        Trank.__init__(self, "Erfahrungstrank", self.erfahrungspunkte * 3)
