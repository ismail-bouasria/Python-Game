# je crée ma classe monster
import pygame


class Monster(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./assets/mummy.png')
        self.velocity = 2
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 540

    def forward(self):
        self.rect.x -= self.velocity