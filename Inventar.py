class Inventar:
    def __init__(self, max_gewicht):
        self.inhalt = []
        self.max_gewicht = max_gewicht
        self.gewicht = 0

    def check(self):
        if self.gewicht > self.max_gewicht:
            self.inhalt.pop()
            self.gewicht -= 1
