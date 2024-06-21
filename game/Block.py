# Block.py
import pygame

class Barrier():
    def __init__(self, x, y, width, height, color=(255, 0, 0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw_barrier(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.display.flip()