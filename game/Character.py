import pygame
from Screen import Screen

class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player = pygame.Rect(50, Screen().screen_height - 200, 50, 50)
        self.x_speed = 5
        self.y_speed = 5

        self.jump_strength = -15
        self.gravity = 2

        self.left = False
        self.right = False
        self.jump = False

    def update(self):
        if self.left:
            self.player.x -= self.x_speed
        if self.right:
            self.player.x += self.x_speed
        if self.jump:
            self.player.y -= self.jump_strength
            self.jump_strength += self.gravity
        else:
            self.jump_strength = -15
            self.player.y += self.jump_strength
