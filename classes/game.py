import pygame.sprite

from .player import Player

from .monster import Monster


# Créer une classe Game

class Game:
    def __init__(self):
        # générer notre joueur
        self.player = Player(self)
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()

    def spawn_monster(self):
        monster = Monster()
        self.all_monsters.add(monster)

        # definir la collision

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
