# importer Pygame et l'initaliser
import pygame
import math
from classes.game import Game

pygame.init()

# Generer la fenêtre du jeu
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

# Importer charger à l'arrière plan
background = pygame.image.load('./assets/bg.jpg')

# Charger notre jeu
game = Game()

running = True

# Boucle tant que cette condition est vrai la fenêtre reste ouverte
while running:
    # appliquer l'arrière plan de notre jeu
    screen.blit(background, (0, -200))

    # Importer et positionner la bannière de début de partie

    banner = pygame.image.load('./assets/banner.png')
    banner = pygame.transform.scale(banner, (500, 500))
    banner_rect = banner.get_rect()
    banner_rect.x = math.ceil(screen.get_width() / 4)

    # Importer le bouton pour lancer la partie
    play_button = pygame.image.load('./assets/button.png')
    play_button = pygame.transform.scale(play_button, (400, 150))
    play_button_rect = play_button.get_rect()
    play_button_rect.x = math.ceil(screen.get_width() / 3.33)
    play_button_rect.y = math.ceil(screen.get_height() / 2)

    # verifier si notre jeu est lancé ou non
    if game.is_playing:
        # déclencher les instructions de la partie
        game.update(screen)
    # verifier
    else:
        # ajouter le bouton de lancement
        screen.blit(play_button, play_button_rect)
        # ajouter mon écran de bienvenue
        screen.blit(banner, banner_rect)

    # mettre à jour l'écran
    pygame.display.flip()

    # si le joueur ferme la fenêtre
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre.
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # détecter si la touche espace est enclenchée pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verifier si la souris est en collision avec le bouton play

            if play_button_rect.collidepoint(event.pos):
                # mettre  le jeu en mode "lancé"
                game.start()
