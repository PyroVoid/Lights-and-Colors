import pygame
import random

class Tree:
    IMAGE = pygame.image.load("tree.webp")  # Replace with your image path

    SCREEN_WIDTH = 616
    SCREEN_HEIGHT = 924

    TREE_TL = (200, 250)
    TREE_BR = (400, 770)

    LIGHTS = 50

    def __init__(self):
        # lights colors
        self.light_colors = []
        # light coords
        self.light_coords = []

        # gen random coords
        for i in range(Tree.LIGHTS):
            x = random.randint(Tree.TREE_TL[0], Tree.TREE_BR[0])
            y = random.randint(Tree.TREE_TL[1], Tree.TREE_BR[1])
            self.light_coords.append((x, y))
            self.light_colors.append((random.randint(0,255), random.randint(0,255), random.randint(0,255)))

    def set_color(self, index, color):
        self.light_colors[index] = color

    # Main loop
    def update(self, screen):
        screen.fill((0, 0, 0))  # Fill screen with black
        screen.blit(Tree.IMAGE, (0, 0))  # Draw image at (x, y)

        # draw lights
        for i in range(Tree.LIGHTS):
            pygame.draw.circle(screen, self.light_colors[i], self.light_coords[i], 10)

        pygame.display.flip()  # Update display