import pygame
from .projectile import Projectile


# Créer une classe Player
class Player(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.game = game
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def launch_projectile(self):
        # créer une instance de la classe projectile

        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        # si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self,self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
