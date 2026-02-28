import pygame
from VirtTree import Tree

pygame.init()
screen = pygame.display.set_mode((Tree.SCREEN_WIDTH, Tree.SCREEN_HEIGHT))

tree = Tree()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    tree.update(screen)

pygame.quit()