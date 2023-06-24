# je crée ma classe monster
import pygame


class Monster(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('./assets/mummy.png')
        self.velocity = 1
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 540

    def forward(self):
        # le déplacement ne se fait pas que s'il n' a pas de collision avec le groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity