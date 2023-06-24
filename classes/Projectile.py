import pygame

# Définir la classe Projectile

class Projectile(pygame.sprite.Sprite):

    #définir le constructeur de la classe
    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load('../assets/projectile.png')
        self.rect = self.image.get_rect()
