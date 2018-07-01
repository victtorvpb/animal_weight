from dj.choices import Choices, Choice


class AnimalChoice(Choices):
    bovino = Choice("Bovino")
    caprino = Choice("Caprino")
    suino = Choice('Suino')
