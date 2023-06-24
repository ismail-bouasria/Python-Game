from .player import Player


# Créer une classe Game

class Game:
    def __init__(self):
        # générer notre joueur
        self.player = Player()
        self.pressed = {}
