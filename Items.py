class Item:
    def __init__(self, weigth, worth):
        self.weight = weigth
        self.worth = worth


class Potion(Item):
    def __init__(self, weight, worth):
        Item.__init__(self, weight, worth)


class HealthPotion(Potion):
    def __init__(self, weight, worth, regenerated_health):
        Potion.__init__(self, weight, worth)
        self.regenerated_health = regenerated_health
