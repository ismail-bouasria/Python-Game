# importer Pygame et l'initaliser
import pygame
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

    # appliquer l'image de mon joueur
    screen.blit(game.player.image, game.player.rect)

    #Récuperer les projectile du joueur

    for projectile in game.player.all_projectiles:
        projectile.move()

    # appliquer l'ensemble des images du groupe de projectiles

    game.player.all_projectiles.draw(screen)

# verifier si le joueur souhaite aller à gauche ou à droite et collision des limites de l'écran

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()
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
