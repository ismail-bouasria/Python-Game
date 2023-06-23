# importer Pygame et l'initaliser
import pygame
pygame.init()

# Generer la fenêtre du jeu
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))
background = pygame.image.load('assets/bg.jpg')
running = True

# boucle tant que cette condition est vrai la fenêtre reste ouverte
while running:
    # appliquer l'arrière plan de notre jeu
    screen.blit(background,(0,-200))

    #mettre à jour l'écran
    pygame.display.flip()

    # si le joueur ferme la fenêtre
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre.
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


