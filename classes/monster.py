# je crée ma classe monster
import pygame
import random


class Monster(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('./assets/mummy.png')
        self.velocity = random.randint(1, 3)
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 100)
        self.rect.y = 540

    def damage(self, amount):
        # Infliger les dégàts
        self.health -= amount

        # Vérifier si son nouveau nombre de point de vie est inférieure ou égal à 0

        if self.health <= 0:
            # Reapparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.max_health
            self.velocity = random.randint(1, 3)

    def update_health_bar(self, surface):
        # definir une couleur pour notre jauge de vie ( vert)
        bar_color = (111, 210, 46)

        # definir une couleur pour la jauge vide
        empty_bar_color = (60, 63, 60)

        # definir la position de la barre de vie et sa taille
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]

        # definir la position de la barre vide et sa taille
        empty_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]

        # dessiner notre barre de vie et barre vide
        pygame.draw.rect(surface, empty_bar_color, empty_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def forward(self):
        # le déplacement ne se fait pas que s'il n' a pas de collision avec le groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre entre en collision avec le joueur
        else:
            # Infliger des dégats au joueur
            self.game.player.damage(self.attack)
