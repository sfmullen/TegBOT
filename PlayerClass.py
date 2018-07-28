class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.countries = set([])
        self.mission = 0
        self.human = True
        self.turn_to_play = False

    def convertToBOT(self):
        self.human = False

    def addCountry(self, country):
        self.countries.add(country)

    def changeColor(self, newColor):
        self.color = newColor
